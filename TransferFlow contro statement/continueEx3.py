#program for extaracting  +Ve from list of numbers
#continueex3.py
lst=[10,-23,45,67,-56,-89,12,23,9,0,-66]
print("List of Possitive Numbers:")
for v in lst:
	if(v<=0):
		continue
	print("\t{}".format(v))