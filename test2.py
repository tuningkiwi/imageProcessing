from mod1 import add

class FourCal:
    def __init__(self,first=0, second=0):
        self.first = first #클래스의 변수는 생성자에서 선언해주기 
        self.second = second
        self.result = 0 
    
    def setdata(self,a,b):
        self.first = a
        self.second = b
    
    def add(self): #클래스 메서드의 아규먼트로 꼭 self 전해주기 
        self.result = self.first + self.second
        return self.result
    
    def sub(self):
        self.result = self.first - self.second
        return self.result
        
    def mul(self):
        self.result = self.first * self.second
        return self.result
        
    def div(self):
        self.result = self.first / self.second
        return self.result
    
    
class MoreForeCal(FourCal): #상속하기 
    def pow(self):
        result = self.first** self.second
        return result 
    
class SafeFoureCal(FourCal): #함수 재정의를 통한 처리 
    def div(self):
        if self.second == 0 :
            return 0
        else: 
            return self.first/self.second

my = SafeFoureCal(4,0)
print("div : {0:.2f}".format(my.div()))
print("add : {0:.2f}".format(my.add()))


print(add(3,1002))
