class Univ:
    def getunivdet(self):
        self.uname=input("Enter Your Nmae:")
        self.uloc=input("Enter your Unvirsity Location:")
    def dispunivdet(self):
        print("*"*50)
        print("University Details:")
        print("*"*50)
        print("University Name:{}".format(self.uname))
        print("University Location:{}".format(self.uloc))
        print("*"*50)
class college(Univ):
    def getcollege(self):
        self.cname=input("Enter Your college Nmae:")
        self.Cloc=input("Enter your College Location:")

    def dispcolldet(self):
        print("*"*50)
        print("College Details:")
        print("*"*50)
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.Cloc))
        print("*"*50)
class Student(college):
    def getstuddet(self):
        self.sno=folat=(input("Enter student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
    def dispstuddet(self):
        print("*"*50)
        print("student Details:")
        print("Student College Number{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("Student Course:{}".format(self.crs))
        print("*"*50)

s=Student()
s.getunivdet()
s.getstuddet()
s. getcollege()
s.dispcolldet()
s.dispstuddet()



        






