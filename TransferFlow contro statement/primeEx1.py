#Program deciding whether the given number of prime or not
#primeex1.py
n=int(input("Enter a number:"))
if(n<=1):
	print("{} is invalid input:".format(n)) #n=2
else:
	assume="prime"
	for i in range(2,n):
		if(n%i==0):
			assume="notprime"
			break

	if(assume=="prime"):
		print("{} is PRIME".format(n))
	else:
		print("{} is NOT PRIME".format(n))
	