import tensorflow as tf
import tflite_runtime.interpreter as tflite
import numpy as np 

#모델 로드 
interpreter = tf.lite.Interpreter(model_path='model.tflite')
#텐서 할당 
interpreter.allocate_tensors()

#모델이 기대하는 입력 데이터 포맷 
input_details = interpreter.get_input_details()
#모델이 기대하는 출력 데이터 포맷 
output_details = interpreter.get_output_details()
print(input_details)
print(output_details)

#입력 데이터(x=10.0)에 대한 y를 예측하려면 입력 배열의 크기와 타입 정의  필요 
to_predict =  np.array([[10.0]],dtype = np.float32)
print(to_predict)

#입력 값을 넣기 위한 입력 텐서 설정 
interpreter.set_tensor(input_details[0]['index'], to_predict)
interpreter.invoke()

#출력 값을 반환 받을 출력 텐서 설정 
tflite_results = interpreter.get_tensor(output_details[0]['index'])
print(tflite_results)


