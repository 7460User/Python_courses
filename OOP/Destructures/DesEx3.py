import sys,time
class Employee:
    def __init__(self,eno,ename):
        print("*"*50)
        self.a=eno
        self.b=ename
        print("\t{}\t{}".format(self.a,self.b))
        print("*"*50)
    def __del__(self):
        print("\tI am garbage calector __del__(self)")
#main program
e1=Employee(10,"Rausam")
e1=None
print("No langer Memory space of e1 object") 
time.sleep(5)
e2=Employee(20,"Sonu")
e3=Employee(30,"Radha")
print("program is a ended:")

          
        