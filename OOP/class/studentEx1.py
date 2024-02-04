#StudentEx1.py
class Student:
	crs="PYTHON"  # Class Level Data Member

#main program
s1=Student()
s2=Student()
print("-"*50)
print("id of s1=",id(s1))
print("id of s2=",id(s2))
print("initial content of s1=",s1.__dict__)#{}
print("initial content of s2=",s2.__dict__)#{}
print("initial number of values in s1=",len(s1.__dict__))#0
print("initial number of values in s2=",len(s2.__dict__))#0
print("-"*50)
#place intance data member in s1 object
s1.stno=10
s1.sname="raja"
s1.mark=58.2
#place intance data member in s2 object
s2.stn0=20
s2.marks= 69.40
s2.smane="aryan"
print("now content of s1=",s1.__dict__)#{}
print("now content of s2=",s2.__dict__)#{}
print("now member of values in s1=",s1.__dict__)#3
print("now member of values in s1=",s2.__dict__)#3
print("commun course for all students =",Student.crs)
print("-"*50)



