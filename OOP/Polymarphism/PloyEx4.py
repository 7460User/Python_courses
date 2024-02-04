
#PloyEx4.py
class Circle:
	def  area(self):  # Original Method--Instance Methods
		self.r=float(input("Enter Radious:"))
		self.ac=3.14*self.r**2
		print("Area of Circle={}".format(self.ac))

class Square:
	def area(self): #Original Method--Instance Methods
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square={}".format(self.sa))
		
class Rect(Square,Circle):
	def  area(self):  # Overridden Method
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		self.ar=self.l*self.b
		print("Area of Rect={}".format(self.ar))
		super().area()
		Circle.area(self)
	
#Main Program
r=Rect()
r.area()