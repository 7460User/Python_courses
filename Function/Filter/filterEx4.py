#write a python program which will filter list of Even numbers
#FilterEx5.py
def readvalues():  # Normal Function Reading Values dynamically
	lst=[]
	noe=int(input("Enter How Many Elements:"))
	if(noe<=0):
		return lst  # empty list
	else:
		for i in range(1,noe+1):
			val=int(input("Enter {} Value:".format(i)))
			lst.append(val)
		return lst   # non-empty list

#Anonymous Function
even=lambda n: (n%2==0) and (n>0)

#main program
lst=readvalues()
if(len(lst)==0):
	print("List empty--we can't do any operations")
else:
	evenlist=list(filter(even,lst))
	print("\nGiven List of Elements:{}".format(lst))
	print("\nEven List of Elements:{}".format(evenlist))