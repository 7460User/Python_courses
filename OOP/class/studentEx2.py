class student:
    crs="python"
s1=student()
s2=student()
#Place Instance Data Members in s1 object (By using object Name)
s1.numb=10
s1.ename="govind"
s1.marks=78.2
#place instance data member in s2 object (by using object name)
s2.numb=20
s2.ename="sonu"
s2.marks=90.4
s2.villege="HYD"
print("-"*50)
print("student information")
print("-"*50)
print("student Number of-->{}".format(s1.numb))
print("Student Name of:--->{}".format(s1.ename))
print("Student Marks of:-->{}".format(s1.marks))
print("-"*50)
print("Student Information")
print("-"*50)
print("Student numb of:--->{}".format(s2.numb))
print("Student Name of:--->{}".format(s2.ename))
print("student marks of:-->{}".format(s2.marks))
print("Student village of->{}".format(s2.villege))
print("-"*50)