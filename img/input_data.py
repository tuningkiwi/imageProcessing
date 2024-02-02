# curl 명령어를 위한 py 파일
from tensorflow.keras.preprocessing import image
import numpy as np
import json

# 이미지 로드 및 전처리

# 이미지 파일의 경로를 지정합니다.
img_path = '..\\image_docker\\cat1.jpg'
# 이미지를 지정된 크기로 로드합니다. target_size는 (150, 150)으로 지정되어 있습니다.
img = image.load_img(img_path, target_size=(224,224 ))
# 이미지를 numpy 배열로 변환합니다.
img_array = image.img_to_array(img)
# 이미지 배열의 차원을 확장하여 모델이 예상하는 입력 형태로 만듭니다.
# 모델은 (1, 150, 150, 3) 형태의 입력을 기대하므로, np.expand_dims 함수를 사용하여 차원을 추가합니다.
img_array = np.expand_dims(img_array, axis=0) 
#이미지의 픽셀 값은 일반적으로 0에서 255 사이의 정수로 표현  0 과 1 사이의 값으로 정규화 
img_array /= 255.0  

# 입력 데이터를 JSON 형식으로 변환
data = {"instances": img_array.tolist()}
# JSON 데이터를 파일에 씁니다.
# "input_data.json" 파일에 JSON 데이터를 씁니다.
with open("input_data.json", "w") as json_file:
    json.dump(data, json_file)