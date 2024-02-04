#This Program demonstrates the functionality of continue statement
#continueex1.py
s="PYTHON"
print("\n------------for loop without continue stmt---------------------------")
for ch in s:
	print("\t{}".format(ch))
else:
	print("i am from else-part-of-for loop")
print("=============================================")
#Display P Y T O N
for ch in s:
	if(ch=="H"):
		continue
	else:
		print("\t{}".format(ch))
else:
	print("i am from else-part-of-for loop")
print("=============================================")	
#Display P Y H N  (s="PYTHON")
for ch in s:
	if(ch=="T") or (ch=="O"):
		continue
	print("\t{}".format(ch))
else:
	print("i am from else-part-of-for loop")
print("=============================================")	
#Display P O N  (s="PYTHON")
for ch in s:
	if (ch=="Y") or (ch=="T") or (ch=="H") :
		continue
	print("\t{}".format(ch))
print("i am from else-part-of-for loop")
print("=============OR==============================")	
#Display P O N  (s="PYTHON")
for ch in s:
	if ch in ["Y","T","H"]:
		continue
	print("\t{}".format(ch))
print("i am from else-part-of-for loop")