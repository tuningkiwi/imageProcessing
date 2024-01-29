###########################
## 라즈베리 파이에서 실행할 파일 
###########################

#import tensorflow as tf 
import tflite_runtime.interpreter as tflite
import tensorflow_datasets as tfds 
import numpy as np 
import matplotlib.pyplot as plt 

#244x 244 사이즈로 리사이즈를 하고, 정규화를 해줍니다. 
def format_image(image,label):
    image = tf.image.resize(image,(224,224))/255.0
    return image, label

#훈련, 검증, 테스트 세트로 나눕니다. 
(raw_train, raw_validation, raw_test), metadata =tfds.load(
    'cats_vs_dogs',
    split=['train[:80%]','train[80%:90%]','train[90%:]'],
    with_info=True,
    as_supervised=True,
)

#테스트 배치 파일을 만들어 줍니다. 
test_batches = raw_test.map(format_image).batch(1)

#모델 로드 
#interpreter = tf.lite.Interpreter(model_path='/content/drive/MyDrive/INTEL_PYTHON/converted_model.tflite')
interpreter = tflite.Interpreter(model_path='converted_model.tflite')

#텐서 할당 
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

predictions =[] 

print(input_index)
print(output_index)

# #모델이 기대하는 입력 데이터 포맷 
# input_details = interpreter.get_input_details()
# #모델이 기대하는 출력 데이터 포맷 
# output_details = interpreter.get_output_details()
# print(input_details)
# print(output_details)



#테스트 해보기
#테스트 배치 파일을 100개 씩 가져와서  
predictions =[] 
test_labels, test_imgs = [],[]
for img, label in test_batches.take(100):
    interpreter.set_tensor(input_index, img)
    interpreter.invoke()
    predictions.append(interpreter.get_tensor(output_index))
    test_labels.append(label.numpy()[0])
    test_imgs.append(img)


#예측 수 비교 
score  = 0 
for item in range(0,99):
    prediction = np.argmax(predictions[item])
    label = test_labels[item]
    if prediction == label:
        score = score +1


print("100개 중 맞은 예측 수: "+ str(score))

class_names = ['cats','dogs']

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    
    # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
    img = tf.squeeze(img) # [2, 3]

    plt.imshow(img)

    predicted_label = np.argmax(predictions_array[index])
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
        
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                    100*np.max(predictions_array),
                                    class_names[true_label]),
                                    color=color)

# for index in range(0,99):
#     plt.figure(figsize = (6,3))
#     plt.subplot(1,2,1)
#     plot_image(index, predictions, test_labels, test_imgs)
#     plt.show() 
#     plt.savefig('boston.png')
#     break


for index in range(0,100):

    if index%2 == 0 :
      plt.figure(figsize = (6,3))
      plt.subplot(121)
    elif index %2 ==1 :
      plt.subplot(122)

    plot_image(index, predictions, test_labels, test_imgs)
    if index %2 ==1:
      plt.show()
      imgFile = 'resultImg/result{}.png'.format(index)
      plt.savefig(imgFile)


