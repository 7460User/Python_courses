class student:
    @classmethod
    def dirrectclass(cls):
        print("-"*50)
        cls.sno=int(input("Enter Student Number:"))
        cls.name=(input("Enter Your Name:"))
        cls.marks=float(input("Enter Your Marks:"))

    @classmethod
    def display(cls):
        print("-"*50)
        print("Student Number:{}".format(cls.sno))
        print("Your Name:{}".format(cls.name))
        print("Yours Marks:{}".format(cls.marks))
        print("*"*50)
student.dirrectclass()
student.display()