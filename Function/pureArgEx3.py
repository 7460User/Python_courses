#Program for demonstrating Variable  length arguments
#PureVarAgrsEx2.py
def  disp( *kvr):  # Here *kvr us called Variable Lengh Parameter and its type is tuple
	print("-"*50)
	print("Number of Values={}".format(len(kvr)))
	for val in kvr:
		print("{}".format(val),end="  ")
	print()
	print("-"*50)

#main program
disp(10) # Function call-1
disp(10,20) # Function call-2
disp(10,20,30) # Function call-3
disp(10,20,30,40) # Function call-4
disp("KVR","PYTHON","JAVA","ADV JAVA","D.Sc") # Function call-5
disp() 