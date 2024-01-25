import random
import numpy as np 

groupNum = [1,2,3,4,12,19,20]

for idx, i in enumerate(range(0,7)):
    
    num = random.randrange(0,7-idx) #index
    #weights = np.arange(0,)
    #num = random.choices(range(0,7-idx),weights=[0.13,0.13,0.13,0.13,0.13,0.13,0.13])
    print(str(idx)+":\t"+str(groupNum[num]))
    groupNum.pop(num) #index 
    



# num = random.randrange(0,7)

# print(groupNum[num])