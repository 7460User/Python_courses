#program for demonstarting globals() 
#globalsfunex1.py
a=10
b=20
c=30
d=40 # Here 'a' 'b' 'c' and 'd' are called Global variables
def operations():
	a=1
	b=2
	c=4
	d=4   # Here 'a' 'b' 'c' and 'd' are called Local variables
	x=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
	print(x)

#main program
operations()


