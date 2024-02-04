#Program for generating Mul tables for list of values.
#InnerLoopsDynamicMultables.py
notables=int(input("Enter How Many tables u want:"))  # n=5
if(notables<=0):
	print("{} Invalid Input".format(notables))
else:
	lst=[]  # or   lst= list()
	print("Enter {} Values for Generating Mul tables:".format(notables))
	for i in range(1,notables+1):
		val=int(input())
		lst.append(val) # adding the values to list object
	else:
		print("-"*50)
		print("List of Values:{}".format(lst))  # List of Values:[13, 23, -4]
		print("-"*50)
		#Code  for generating Mul tables
		for n in lst:
			if(n<=0):
				print("{} is invalid input:".format(n))
			else:
				print("-"*50)
				print("\tMul Table for :{}".format(n))
				print("-"*50)
				for i in range(1,11):
					print("\t{} x {}={}".format(n,i,n*i))
				else:
					print("-"*50)
