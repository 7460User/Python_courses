#Program for demonstrating global keyword
#GlobalKwdEx3.py

def update1():
	global a,b
	a=a+1
	b=b+1

def update2():
	global a,b
	a=a*2
	b=b*2

#main program
a,b=10,20 # here 'a' and 'b'  are called Global Variable
print("Val of Global Vars in main program before update1 a:{},b:{}".format(a,b)) # a=10 b=20
update1()
print("Val of Global Var in main program after update1 a:{}, b:{} ".format(a,b)) # a=11 b=21
update2()
print("Val of Global Var in main program after update2 a:{},b:{} ".format(a,b)) # a=22, b=42