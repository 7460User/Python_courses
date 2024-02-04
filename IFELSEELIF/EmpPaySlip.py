#Program generating pay slip
#EmpPaySlip.py
eno=int(input("Enter Emploee Number:"))
ename=input("Enter Emploee Name:")
basicsal=float(input("Enter Emploee Basic Salary:"))# 12000
cname=input("Enter Emploee Company Name:")
if(basicsal<0):
	print("{} is Invalid salary:".format(basicsal))
else:
					#Cal the Other Benifits of employee whose basic sal is >=10000
	if(basicsal>=10000):
		ta=basicsal*(10/100)
		da=basicsal*(20/100)
		hra=basicsal*(16/100)
		ma=basicsal*(2/100)
		lic=basicsal*(1/100)
		gpf=basicsal*(1/100)
	else:
		ta=basicsal*(5/100)
		da=basicsal*(10/100)
		hra=basicsal*(8/100)
		ma=basicsal*(2/100)
		lic=basicsal*(0.5/100)
		gpf=basicsal*(1/100)
	netsal=(basicsal+ta+da+hra+ma)-(lic+gpf)
	#Display Pay Slip of an employee
	print("-"*50)
	print("\tEmployee Pay Slip")
	print("-"*50)
	print("\tEmployee Number:{}".format(eno))
	print("\tEmployee Name:{}".format(ename))
	print("\tEmployee Company Name:{}".format(cname))
	print("\tEmployee Basic Salary:{}".format(basicsal))
	print("\tEmployee TA:{}".format(ta))
	print("\tEmployee DA:{}".format(da))
	print("\tEmployee HRA:{}".format(hra))
	print("\tEmployee MA:{}".format(ma))
	print("Employee DEDUCTIONS:")
	print("\tEmployee LIC:{}".format(lic))
	print("\tEmployee GPF:{}".format(gpf))
	print("-"*50)
	print("\tEmployee Net Salary:{}".format(netsal))
	print("-"*50)