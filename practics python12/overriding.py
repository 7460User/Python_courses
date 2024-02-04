class Student:
    def good(self):
        print("\tThis is first class")
class Child(Student):
    def good(self):
        print("\tThis my decound class")
        super().good() 

class parent(Child):
    def good(self):
        print("\t this is my third class")
        super().good() 

class pankaj(parent):
    def good(self):
        print("\tThis is my forth class")
        super().good() 

class sonu(pankaj):
    def good(self):
        print("\tThis is my fourth class")
        super().good()                        
# main program  
s1=sonu()  
s1.good()