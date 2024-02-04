class student:
    def addnumber(self):
        print("-"*50)
        self.a=int(input("Enter Any Number a:"))
        self.b=int(input("Enter Any Number b:"))
        self.c=(self.a)+(self.b)
        print(self.c)
    def display(self):
        print("-"*50)
        print("a value",self.a)
        print("b value",self.b)
        self.c=(self.a)+(self.b)
        print(self.c)

a=student()
a.addnumber()
a.display()
