#write a python program which will calculate simple interest and total amount to pay by using functions
#SimpleIntFunEx1.py
def  simpleint():
	p=float(input("Enter Principle Amount:"))
	t=float(input("Enter  Time:"))
	r=float(input("Enter Rate of Interest:"))
	#cal  si and totamt
	si=(p*t*r)/100
	totamt=p+si
	return p,t,r,si,totamt

#main program
res=simpleint()
print("="*40)
print("Simple Interest Calculations")
print("="*40)
print("Principle Amount:{}".format(res[0]))
print("Time:{}".format(res[1]))
print("Rate of Interest:{}".format(res[2]))
print("Simple  Interest:{}".format(res[3]))
print("Total Amount to Pay:{}".format(res[4]))
print("="*40)