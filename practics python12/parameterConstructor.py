class Parameter:
    def __init__(self,a,b):
        print("i am from parameterized constructor:")
        self.a=a
        self.b=b
        print("value of a:{}".format(self.a))
        print("value of b:{}".format(self.b))
p=Parameter(20,10)
p1=Parameter(40,4)
p2=Parameter(80,90,30,40)
        