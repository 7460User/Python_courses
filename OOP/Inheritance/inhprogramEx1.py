class c1:
    def getA(self):
        self.a=10
        self.b=20
       
class c2(c1):
    def getB(self):
        self.b=40
        self.a=50
        self.ename="govind"
       
s1=c2()
print(s1.__dict__)               
s1.getA()
print("content of s1=",s1.__dict__)
s1.getA()
print("content of s1=",s1.__dict__)
s1.getB()
print("content of s1=",s1.__dict__)
