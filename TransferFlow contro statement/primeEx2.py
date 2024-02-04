#Program deciding whether the given number of prime or not
#primeex2.py
n=int(input("Enter a number:"))
if(n<=1):
	print("{} is invalid input:".format(n)) #n=2
else:
	res=False
	for i in range(2,n):
		if(n%i==0):
			res=True
			break

	if(res==False):
		print("{} is PRIME".format(n))
	else:
		print("{} is NOT PRIME".format(n))