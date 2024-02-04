#Program for demonstrating Dest6ructor
#DestEx2.py
import sys,time
class Employee:
	def  __init__(self,eno,ename):   #  Constructor Def
		print("-"*50)
		print("\tI am from Constructor:")
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))
		print("-"*50)
	def __del__(self):   # Destructor Def
		global totmemspace
		print("\nI am GC Calling    __del__(self)")
		print("Total Memory space of Program before programe exec ended=",totmemspace)
		totmemspace=totmemspace-sys.getsizeof(self)
		print("Now Memory space Available:",totmemspace)

#main program
print("Program execution started")
e1=Employee(10,"Rossum") # Object Creation-PVM calls Constructor
e2=Employee(20,"Travis") # Object Creation-PVM calls Constructor
e3=Employee(30,"Kinney") # Object Creation-PVM calls Constructor
print("Program execution ended")
totmemspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
time.sleep(10)
#Here once the program execution is over, Automatically GC calls Destructor and this type calling of Desructor is called Automatic Garbage Collection.