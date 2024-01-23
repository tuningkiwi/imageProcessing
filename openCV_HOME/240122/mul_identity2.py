import numpy as np 

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
ainv = np.linalg.inv(a)
c = np.array([[1,2],[3,4]])
cinv = np.linalg.inv(c)

# print(a.dot(b))
# print(a*b)

print(np.dot(a,ainv),np.eye(3))
np.allclose(np.dot(ainv, a), np.eye(3))
#print(np.dot(a,b))