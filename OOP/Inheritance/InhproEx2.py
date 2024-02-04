#InhProg2.py
class C1:  # Base Class
	def  getA(self):
		self.a=10
        

class C2(C1):  # Derived Class
	def getB(self):
		self.b=20
   
		self.getA() # We are calling Base class getA()
		self.dispAB()# are calling current class dispAB()
	def dispAB(self):
		print("Val of a--C1-BC: {}".format(self.a))
		print("Val of b--C2-DC: {}".format(self.b))
      

# main program
s1=C2()
s1.getB()