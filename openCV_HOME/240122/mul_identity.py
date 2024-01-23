import numpy as np 

a= np.array([[1,2,3],[4,5,6]])
b= np.array([[7,8],[9,10],[11,12]])

#행렬의 곱은 순서에 따른 다른 결과값
print(a.dot(b))
print(b.dot(a))

a= np.array([[1,2],[4,5]])
#b= np.array([[1,2,3],[4,5,6],[7,8,9]])
b= np.array([[1,2],[1,5]])

print(a.dot(b)) 
print(np.dot(a,b))
print(b.dot(a))

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a*b)

#b = np.array([4,5]) 크기가 맞지 않기 때문에 에러남 
#print(a*b)

print(np.identity(3))

a= np.array([[1,2],[4,5]])
b= np.array(np.identity(2))
print(a.dot(b))

a= np.array([[1,2],[4,5],[6,7]])
b= np.array(np.identity(2))
print(a.dot(b))

