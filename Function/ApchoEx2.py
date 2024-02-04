#Program addition of Two Numbers  c=a+b
#ApproachEx2.py
#Key Points:    Input : Taking in Function Body      
#						 Process:   Doing Function Body
#						 Result		:  Displaying Function Body

def  sumop():
	# taking Input--Function Body
	a=float(input("Enter First Value:"))
	b=float(input("Enter Second Value:"))  
	#Process the input
	c=a+b  # Here 'a' 'b' and 'c' are called Local Variables
	#display the result in function body
	print("sum({},{})={}".format(a,b,c))

#main program
sumop() # Function Call
