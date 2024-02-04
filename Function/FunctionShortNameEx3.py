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
		#By using OUR OWN LOGIC--Selection Sort
		for i in range(0,len(lst)):
			for j in range(i+1,len(lst)):
				if(lst[i]>lst[j]):
					t=lst[i]
					lst[i]=lst[j]
					lst[j]=t
		else:
			print("Sorted Elements in Asc Order={}".format(lst))
			print("Sorted Elements in DESC Order={}".format(lst[::-1]))

#main program
lst=readvalues()
sortvalues(lst)