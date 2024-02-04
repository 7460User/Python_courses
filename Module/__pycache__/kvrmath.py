#kvrmath.py--File Name and Acts as Module Name
def multable(n):
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		print("-"*50)
		print("Mul table for {}".format(n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		print("-"*50)

def  fact(n):
	if(n<0):
		print("-Ve Number does not have Factorial")
	else:
		f=1
		for i in range(1,n+1):
			f=f*i
		else:
			print("Factorial({})={}".format(n,f))