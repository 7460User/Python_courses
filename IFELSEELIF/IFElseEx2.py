a=int(input("Enter The Value a:"))#1000
b=int(input("Enter The Value b:"))#50
if(a>b):
	print("\tBig Value {},{}={}".format(a,b,a))
res=a if a>b else b if b>a else "Both Number Equel"
print("\t({},{})={}".format(a,b,res))




