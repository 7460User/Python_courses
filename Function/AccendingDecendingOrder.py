def   readvalues():
	lst=[] 
	n=int(input("Enter How Many Values u want to Sort:"))
	if(n<=0):
		return lst
	else:
		for i in range(1,n+1):
			val=int(input("Enter {} Value:".format(i)))
			lst.append(val)
		return lst  
def sortvalues(lst):
    if(len(lst)==0):
        print("List is empty can't short any values:")
    else:
        print("Given values:{}".format(lst))
        lst.sort()
        print("Sorted Names in Ascending Order :{}".format(lst))
        lst.sort(reverse=True)
        print("Sorted Values in Decending Order :{}".format(lst))
lst=readvalues()
sortvalues(lst)  



