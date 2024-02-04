class Student:
    def readdata(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=(input("Enter Student Name:"))
        self.marks=float(input("Enter Student Marks:"))
        self.add=input("Enter Student Addresh:")
class Employee:
    def employeeinfo(self):
        self.sno=int(input("Enter Employee Number:"))
        self.name=input("enter Employee Name:")
        self.tech=input("Enter Technology Name:")
class Hyd:
	@staticmethod
	def dispobjectdata( kvr ):
		print("-"*50)
		for k,v in kvr.__dict__.items():
			print("\t{}--->{}".format(k,v))
		print("-"*50)
s=Student()
e=Employee()
print("-"*50)
s.readdata()
print("-"*50)
e.employeeinfo() 
print("-"*50)
Hyd.dispobjectdata(s)
Hyd.dispobjectdata(e)  
                
