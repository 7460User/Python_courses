#program for demonstrating Multi Level Inheritance
#InhProg3.py
class GrandParent:  # Base Class
	def getGrandProp(self):
   
		self.gprop=float(input("Enter Grand Parent Properties:"))

class Parent(GrandParent): # Intermediate Base Class
	def getParentProp(self):
		self.pprop=float(input("Enter  Parent Properties:"))

class Child(Parent):  # Derived Class
	def  getChildProp(self):
		self.cprop=float(input("Enter Child Properties:"))
	
	def gettotalproperties(self):
		self.getChildProp()
		self.getParentProp()
		self.getGrandProp()
		self.totprop=self.cprop+self.pprop+self.gprop
		print("Total Property of Child={}".format(self.totprop))


# main program
c=Child()
c.gettotalproperties()



