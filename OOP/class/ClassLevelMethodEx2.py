class student:
    @classmethod
    def level(self):
        self.name="bestTechnology"


    @classmethod
    def level2(cls):
        cls.usre="Full Stack Developer"

    def display(self):
        print("-"*50)
        print("\t1.Your Best Techno:{}".format(self.name))
        print("-"*50)
        print("\t2.This time work:{}".format(self.usre))
        print("-"*50)

student.level()
student.level2()
s1=student()
s1.display()

