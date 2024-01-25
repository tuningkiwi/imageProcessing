import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten,Dense
from tensorflow.keras.optimizers import Adam
import pathlib 

myLayer = Dense(units=1, input_shape=[1])
model = Sequential([myLayer])
model.compile(
    optimizer='sgd',
    loss = 'mean_squared_error'
)

xs = np.array([-1.0,0.0,1.0,2.0,3.0,4.0],dtype=float)
ys = np.array([-3.0,-1.0,1.0,3.0,5.0,7.0],dtype = float)

model.fit(xs,ys,epochs=500)

print(model.predict([10.0]))
print("학습된 가중치: {}".format(myLayer.get_weights()))


#모델 저장하기  
export_dir='saved_model/1' #디렉토리 생성해줌 
tf.saved_model.save(model,export_dir)


#모델 변환하기 
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert() #tflite 모델로 저장하기 

#.tflite 모델로 저장하기 
tflite_model_file = pathlib.Path('model.tflite')
tflite_model_file.write_bytes(tflite_model)