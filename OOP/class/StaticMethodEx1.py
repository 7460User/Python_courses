class Student:
    def studentinfo(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=input("Enter Student Name:")


class Employee:
    def employeeinfo(self):
        self.sno=int(input("Enter Employee Number:"))
        self.name=input("Enter Employee Name:")
        self.sal=float(input("Enter emp Salary:"))

class Teacher:
    def teacherinfo(self):
        self.sno=int(input("Enter Teacher Number:"))
        self.name=input("Enter Teacher Name:")
        self.sub=(input("Enter Teacher Subject Name:"))

class Hyd:
	@staticmethod
	def dispobjectdata( kvr ):
		print("-"*50)
		for k,v in kvr.__dict__.items():
			print("\t{}--->{}".format(k,v))
		print("-"*50)

s=Student()
e=Employee()
t=Teacher()
print("-"*50)
s.studentinfo()
print("-"*50)
e.employeeinfo()
print("-"*50)
t.teacherinfo()
print("-"*50)
Hyd.dispobjectdata(s)
Hyd.dispobjectdata(e)
Hyd.dispobjectdata(t)




