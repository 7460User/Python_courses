#main program
#DivDemo.py
from divop import division
from kvr import KvrDivisionError
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
try:
	c=division(a,b) # Function Call  
except KvrDivisionError:  # Handling the exception.
	print("DON'T ENTER ZERO FOR DEN..")
else:
	print("Div=",c)
finally:
	print("My  finally block")