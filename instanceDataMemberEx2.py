class student:
    def readstudinfo(self):
        print("-"*50)
        self.sno=int(input("Enter Your Number:"))
        self.name=input("Enter your Name:")
        self.marks=float(input("You Marks:"))
        self.add=input("Inter You Location:")
    def dispstudinfo(self):
        print("-"*50)
        print("Your Number:{}".format(self.sno))
        print("Your Number:{}".format(self.name))
        print("Your Marks:{}".format(self.marks)) 
        print("Your address:{}".format(self.add))
s1=student()
s2=student()
s1.readstudinfo() 
s2.readstudinfo() 
s1.dispstudinfo() 
s2.dispstudinfo() 
