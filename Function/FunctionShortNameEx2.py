#write a python program which will accept list of Values and display them in sorted order
#FunSortNamesEx2.py
def   readvalues():
	lst=[] # create an empty list for placing values
	n=int(input("Enter How Many Values u want to Sort:"))
	if(n<=0):
		return lst # empty list
	else:
		for i in range(1,n+1):
			val=int(input("Enter {} Value:".format(i)))
			lst.append(val)
		return lst  # non-empty list

def  sortvalues(lst):
	if(len(lst)==0):
		print("List is empty, can't sort any Values:")
	else:
		print("Given Values:{}".format(lst))
		#By using Pre-defined Functions---sort()  or  sort(reverse=True)
		lst.sort()
		print("Sorted Values in Ascending Order :{}".format(lst))
		lst.sort(reverse=True) #   lst[::-1]  or lst.reverse()
		print("Sorted Values in Decending Order :{}".format(lst))

#main program
lst=readvalues()
sortvalues(lst)