class student:
    @classmethod
    def getcollname(cls):
        cls.uname="OUTER"

    @classmethod
    def getcrsname(cls):
            student.crs="PYTHON"
    def readstudentdata(self):
            print("-"*50)
            self.eno=int(input("Enter Sudent Number:"))
            self.name=(input("Enter Your Name:")) 
            self.marks=float(input("Enter Your Marks:"))
    def display(self):
            print("-"*50)
            print("student Number:{}".format(self.eno))
            print("student Name:{}".format(self.name))
            print("yours marks:{}".format(self.marks))
            print("your unvi..Name:{}".format(self.uname))
            print("Your course:{}".format(self.crs))
student.getcollname()
student.getcrsname()
s1=student()
s2=student()
s1.readstudentdata()
s1.display()


