#write a python program which will accept list of values and find their sum and avg using function
#FunSumAvgEx1.py
def   readvalues():
	lst=[] # create an empty list for placing values
	n=int(input("Enter How Many values u want to enter:"))
	if(n<=0):
		return lst # empty list
	else:
		for i in range(1,n+1):
			val=float(input("Enter {} Value:".format(i)))
			lst.append(val)
		return lst  # non-empty list

def  findsumavg(kvrlst):
	if(len(kvrlst)==0):
		print("List is empty and can't find Sum and Avg:")
	else:   
		#Find Sum and Avg
		s=0
		for val in kvrlst:
			s=s+val
		else:
			print("Given List of Elements:{}".format(kvrlst))
			print("Sum:{}".format(s))
			print("Average:{}".format(s/len(kvrlst)))

#main program
lst=readvalues()
findsumavg(lst)
