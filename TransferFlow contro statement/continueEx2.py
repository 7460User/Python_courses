#This Program demonstrates the functionality of continue statement
#continueex2.py
for i in range(1,6):
	if(i==2) or (i==4):
		print("*"*30)
		print("i am from continue statement Iteration No:{}".format(i))
		continue
	print("\nIteration No:{} out of continue:".format(i))
	print("Python programming")
else:
	print("i am from else-part of for loop")