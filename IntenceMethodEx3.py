#InstanceMethodsEx1.py
class Student:
	def  readstudinfo(self):
		print("-"*50)
		print("in readstudinfo()--id of current object in self=",id(self))
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		print("-"*50)
	def dispstudinfo(self):
		print("-"*50)
		print("in readstudinfo()--id of current object in kvr=",id(self))
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Marks:{}".format(self.marks))
		print("-"*50)

#main program
s1=Student()
s2=Student()
s1.readstudinfo() # Method Call
s2.readstudinfo() # method Call
s1.dispstudinfo() # Method Call
s2.dispstudinfo() # Method Call