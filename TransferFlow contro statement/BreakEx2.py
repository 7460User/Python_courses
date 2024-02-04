#This Program demonstrates the functionality of break statement
#breakex2.py
lst=[10,20,30,40,50,60,70,80,90]


print("\n------------for loop without break stmt---------------------------")
for v in lst:
	print("\t{}".format(v))
else:
	print("i am from else-part-of-for loop")
print("\n------------for loop with break stmt---------------------------")
#display PYT
for v in lst:
	if(v==30):
		break
	else:
		print("\t{}".format(v))
else:
	print("i am from else-part-of-for loop")

print("\nOther statements in Program")