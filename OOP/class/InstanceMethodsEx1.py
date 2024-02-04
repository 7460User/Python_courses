class student:
    def instancemethod(self):
        print("-"*50)
        print("in instancemethod()--id of current object in self =",id (self))
        self.sno=int(input("Enter sno:"))
        self.name=input("Enter your name:")
        self.marks=float(input("Enter Your marks:"))
    def display(self):
        print("-"*50)
        print("Your sno:{}".format(self.sno))
        print("Your name:{}".format(self.name))
        print("Your marks:{}".format(self.marks))

s1=student()

s1.instancemethod()
s1.display() 
      
