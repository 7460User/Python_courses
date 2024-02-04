#Program for demonstrating global keyword
#GlobalKwdEx2.py
def update1():
	global a
	a=a+1

def update2():
	global a
	a=a*2


#main program
a=10 # here 'a' is called Global Variable
print("Val of Global Var in main program before update1 :{} ".format(a)) # 10
update1()
print("Val of Global Var in main program after update1 :{} ".format(a)) # 11
update2()
print("Val of Global Var in main program after update2 :{} ".format(a)) # 22