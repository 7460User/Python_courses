#write a python program which will accept list of names and display them in sorted order
#FunSortNamesEx1.py
def   readvalues():
	lst=[] # create an empty list for placing values
	n=int(input("Enter How Many Names u want to Sort:"))
	if(n<=0):
		return lst # empty list
	else:
		for i in range(1,n+1):
			val=input("Enter {} Name:".format(i))
			lst.append(val)
		return lst  # non-empty list

def  sortvalues(lst):
	if(len(lst)==0):
		print("List is empty, can't sort any names:")
	else:
		print("Given Names:{}".format(lst))
		#By using Pre-defined Functions---sort()  or  sort(reverse=True)
		lst.sort()
		print("Sorted Names in Ascending Order :{}".format(lst))
		lst.sort(reverse=True) #   lst[::-1]  or lst.reverse()
		print("Sorted Names in Decending Order :{}".format(lst))

#main program
lst=readvalues()