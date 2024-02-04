class c1:
    def getA(self):
        self.a=20
        self.b=30
        self.c=40
class c2(c1):
    def getB(self):
        self.ename="govind"
        self.eno=108
s=c2()
print(s.__dict__)
s.getB()
print("Your Name Detail:",s.__dict__)
s.getA()
print("Value of ",s.__dict__)       

