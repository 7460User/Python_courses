import sys,time

class employee:
    def __init__(self,eno,ename):
        print("\tThis is Constructor:")
        self.eno=eno
        self.ename=ename
        print("\t{},{}".format(eno,ename))
    def __del__(self):
        print("\tI am gc calling__del__(self)")
print("Program exection started:")
s1=employee(10,"rassom")
s2=employee(20,"pankaj")
s3=employee(30,"rahul")
print("program exection ended:")
time.sleep(5)  
      