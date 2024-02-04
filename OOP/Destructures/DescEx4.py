#Program for demonstrating Dest6ructor
#DestEx4.py
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
		print("\nI am GC Calling    __del__(self)")
#main program
print("Program execution started")
e1=Employee(10,"Rossum") # Object Creation-PVM calls Constructor
print("No Longer Interested to maintain the memory space of e1 object")
time.sleep(5)
e1=None # Forcefully calling GC for removing the memory space of e1 object
e2=Employee(20,"Travis") # Object Creation-PVM calls Constructor
print("No Longer Interested to maintain the memory space of e2 object")
time.sleep(5)
e2=None # Forcefully calling GC for removing the memory space of e1 object
e3=Employee(30,"Kinney") # Object Creation-PVM calls Constructor
print("No Longer Interested to maintain the memory space of e3 object")
time.sleep(5)
e3=None # Forcefully calling GC for removing the memory space of e1 object
print("Program execution ended")