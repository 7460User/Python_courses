#Program reading any numerical value and find reverse of that value
#ReverseValEx2.py
n=int(input("Enter any val:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("Original value:{}".format(n)) # 3456-------------------------
	rv=0
	while(n>0):
		d=n%10
		rv=rv*10+d
		n=n//10
	else:
		print("Reversed Number:{}".format(rv))
