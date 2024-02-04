#MapEx2.py
def  hike(sal):
	sal=sal+sal*(20/100)
	return sal

#main program
print("Enter list old Salaries of Employees:")
oldsallist=[ float(sal) for sal in input().split()  if float(sal)>0]
newsallist=list(map(hike,oldsallist))
print("\nOld Sal List=",oldsallist)
print("\nNew Sal List=",newsallist)