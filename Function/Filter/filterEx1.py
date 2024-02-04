#write a python program which will filter list of positive nos
#FilterEx1.py
def  posfun(n):
	if n>0:
		return True
	else:
		return False

def  negfun(n):
	if n<0:
		return True
	else:
		return False



lst=[10,-20,34,-56,12,0,-45]
fobj1=filter(posfun,lst)
fobj2=filter(negfun,lst)
print("Type of fobj=",type(fobj1))
print("Content of fobj=",fobj1) 

pslist=list(fobj1)
nslist=tuple(fobj2)
print("\nGiven List of Elements:{}".format(lst))
print("\nPossitive List of Elements:{}".format(pslist))
print("\nNegative List of Elements:{}".format(nslist))