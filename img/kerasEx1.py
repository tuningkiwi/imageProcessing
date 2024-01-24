import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt 

#이미지 디렉토리 위치 저장
train_dir='../cat_dog_small/train'
validation_dir='../cat_dog_small/validation'

#데이터 생성 
train_datagen = ImageDataGenerator(rescale=1/255) #0~1까지 정규화 
validation_datagen = ImageDataGenerator(rescale=1/255) 

#설정 
train_generator = train_datagen.flow_from_directory(
    train_dir,
    classes=['cats','dogs'], #클래스 지정: 타겟, 레이블
    target_size=(150,150),  
    batch_size = 20, #한번에 몇개 사이즈를 갖고 올 것인가 
    class_mode = 'binary', #0 아니면 1 개아니면 고양이를 구별하는 거라 
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    classes=['cats','dogs'], #클래스 지정: 타겟, 레이블
    target_size=(150,150),  
    batch_size = 20, #한번에 몇개 사이즈를 갖고 올 것인가 
    class_mode = 'binary', #0 아니면 1 개아니면 고양이를 구별하는 거라 
)

#한번에 30개 이미지 가져와서 

fig = plt.figure()
axs = []
for i in range(20):
    axs.append(fig.add_subplot(4,5,i+1))

for data_batch,label_batch in train_generator: 
    print(data_batch.shape)   
    print(label_batch.shape)
    print(label_batch) 

    for idx, img_data in enumerate(data_batch):
        axs[idx].imshow(img_data)
    
    break


plt.show()