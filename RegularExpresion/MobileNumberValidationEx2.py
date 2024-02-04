#write a python program which will evaluate mobile number by using Reg Ex
#MobileNumberValidationEx1.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search("\d{10}",mno)
		if(res!=None):
			print("Ur Mobile Number is valid")
			break
		else:
			print("Ur Mobile Number should not contain alphabets and symbols")
	else:
		print("Mobile Number must contains 10 digits length-try again")