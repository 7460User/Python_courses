#Program for generating Student Marks Report
#StudentMarksReportEx2.py

#Validation of student number
while(True):
	sno=int(input("Enter Student Number(100--200):"))
	if(sno>=100) and (sno<=200):
		break
	print("Invalid Student Number:")

sname=input("Enter Student Name:")

#Validation of C(0--100) Lang Marks
while(True):
	cm=int(input("Enter Marks in C:"))
	if(cm>=0) and (cm<=100):
		break
	print("Invalid Marks in C Lang:")

#Validation of C++(0--100) Lang Marks
while(True):
	cppm=int(input("Enter Marks in C++:"))
	if(cppm>=0) and (cppm<=100):
		break
	print("Invalid Marks in C++ Lang:")

#Validation of Python(0--100) Lang Marks
while(True):
	pym=int(input("Enter Marks in Python:"))
	if(pym>=0) and (pym<=100):
		break
	print("Invalid Marks in Python Lang:")
#claculate totmarks
totmarks=cm+cppm+pym
percent=(totmarks/300)*100
#Decide the grade
if(cm<40):
	fs1="C-FAIL"
if(cppm<40):
	fs2="C++-FAIL"
if(pym<40):
	fs3="PYTHON-FAIL"
if(cm<40) or  (cppm<40)  or  (pym<40) :
	grade="FAIL"
if(cm>=40):
	fs1="C-PASS"
if(cppm>=40):
	fs2="C++-PASS"
if(pym>=40):
	fs3="PYTHON-PASS"
if(cm>=40) and (cppm>=40) and (pym>=40):
	if(totmarks<=300) and (totmarks>=250):
		grade="DISTINCTION"
	elif(totmarks<=249) and (totmarks>=200):
		grade="FIRST"
	elif(totmarks<=199) and (totmarks>=150):
		grade="SECOND"
	elif(totmarks<=149) and (totmarks>=120):
		grade="THIRD"

#Display Student Marks Report
print("="*50)
print("\tStudent Marks Report")
print("="*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{} and Result:{}".format(cm,fs1))
print("\tStudent Marks in C++:{} and Result:{}".format(cppm,fs2))
print("\tStudent Marks in Python:{} and Result:{}".format(pym,fs3))
print("-"*50)
print("\tStudent Total Marks:{}".format(totmarks))
print("\tStudent Percentage of Marks:{}".format(percent))
print("\tStudent Grade:{}".format(grade))
print("="*50)