###############################
# colab에서 실행 필요 : 동적 범위 양자화 (dynamic range quantization)
################################

import numpy as np 
import matplotlib.pylab as plt 
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

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


num_examples = metadata.splits['train'].num_examples
num_classes = metadata.features['label'].num_classes

BATCH_SIZE = 32
train_batches = raw_train.shuffle(num_examples//4).map(format_image).batch(BATCH_SIZE).prefetch(1)

validation_batches = raw_validation.map(format_image).batch(BATCH_SIZE).prefetch(1)

test_batches = raw_test.map(format_image).batch(1)

#텐서플로우 허브에 있는 mobilenet_v2 모델을 사용해 feature_extractor라는 케라스 층을 만듭니다. 
#신경망의 첫번째 층 
handle_base, pixels, FV_SIZE = ("mobilenet_v2", 224, 1280)

MODULE_HANDLE = "https://tfhub.dev/google/tf2-preview/{}/feature_vector/4".format(handle_base)

IMAGE_SIZE =(pixels, pixels)


feature_extractor = hub.KerasLayer(
    MODULE_HANDLE,
    input_shape = IMAGE_SIZE +(3,),
    output_shape = [FV_SIZE],
    trainable = False
)

# 모델 선언 
model = tf.keras.Sequential([
    feature_extractor,
    tf.keras.layers.Dense(num_classes, activation ='softmax')
])

model.compile(
    optimizer='adam',
    loss ='sparse_categorical_crossentropy',
    metrics =['accuracy']
)

hist = model.fit(
    train_batches, 
    epochs = 5,
    validation_data = validation_batches
)

#학습된 모델 저장하기
#colab 버전 
#CATS_VS_DOGS_SAVED_MODEL = "/content/drive/MyDrive/INTEL_PYTHON/exp_saved_model" 
#pc 버전 
CATS_VS_DOGS_SAVED_MODEL = 'fiq_exp_saved_model'
tf.saved_model.save(model, CATS_VS_DOGS_SAVED_MODEL)


#tensoflow lite로 변환하기
converter = tf.lite.TFLiteConverter.from_saved_model(CATS_VS_DOGS_SAVED_MODEL)
converter.optimizations = [tf.lite.Optimize.Default]

def representative_data_gen():
    for input_value in test_batches.take(100):
        yield[input_value]

converter.representative_dataset = representative_data_gen
#모델의 가중치를 32비트 실수에서 9비트 정수로 바꿉니다. 
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]

tflite_model = converter.convert()
tflite_model_file = 'fiq_converted_model.tflite'
with open(tflite_model_file, "wb") as f:
  f.write(tflite_model)
