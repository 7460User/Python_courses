class Student:
    def bigandsmallnumber(self):
        print("*"*30)
        self.a=int(input("Enter Number a:"))
        self.b=int(input("Enter Number b:"))
        self.c=int(input("Enter Number c:"))
        print("*"*30)
    def checkbigandsmall(self):
        big=self.a if(self.b<self.a>=self.c) else self.b if(self.a<self.b>=self.c) else self.c if (self.a<=self.c>self.b) else "all values are equal"
        print("big({},{},{})={}".format(self.a,self.b,self.c,big))
    def findsmall(self):
        small=self.a if(self.b>=self.a<self.c) else self.b if(self.a>self.b<=self.c) else self.c if(self.a>=self.c<self.b) else "all values are equal"
        print("Small({},{},{})={}".format(self.a,self.b,self.c,small))
s=Student()
s.bigandsmallnumber()
s.checkbigandsmall()  
s.findsmall()      
