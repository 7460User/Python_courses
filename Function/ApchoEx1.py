
def  sum(a,b): 
	c=a,b 
	return c 

#main program
k=int(input("Enter First Value:"))
v=int(input("Enter Second Value:"))
res=sum(k,v)  # Function Call
print("sum({}+{})={}".format(res,k,v))