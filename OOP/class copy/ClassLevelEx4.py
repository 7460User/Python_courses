class student:
    @classmethod
    def classlevel(cls):
        cls.unvi="Mahatma Gandhi Kashi Vidhyapeeth Varanasi"
    @classmethod
    def dirrectobject(cls):
        cls.clg="Dr.Ghanshyam Shingh PG College varanasi"
    def display(self):
        print("*"*70)
        print("\tA.Your unvirsty name:{}".format(self.unvi))
        print("*"*70)
        print("\tB.Your college Name:{}".format(self.clg))    
        print("*"*70)    
student.classlevel()
student.dirrectobject()
s1=student()
s1.display()


