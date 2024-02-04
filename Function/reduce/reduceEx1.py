#reduceex1.py
import functools
def sumop(k,v):
	return k+v

#main program
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split() if not val.isalpha()]
res=functools.reduce(sumop,lst)
print("sum({})={}".format(lst,res))    