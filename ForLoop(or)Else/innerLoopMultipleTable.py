#Program for generating Mul tables for list of values.
#InnerLoopsMultables.py
lst=[0,12,-6,5,2,-4,19]
for n in lst: #Outer for loop select value from lst and supply to inner  for loop
	if(n>0):
		print("{} is invalid input:".format(n))
	else:
		print("-"*50)
		print("\tMul Table for :{}".format(n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		else:
			print("-"*50)