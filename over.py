class Student():
    def __init__(self):
       print("hello mr. rahul")
class child(Student):
    def __init__(self):
        print("hello two")
class parent(child):
    print("hello three")

s1=parent()
s2=Student()