class Student:
    def draw(self):
        print("\tHello i am overding handling")
    

class React(Student):
    def draw(self):
        print("\tMy second program")
        super().draw()

class Sub(React):
    def draw(self):
        print("\tMy third program") 
        super().draw()

class Super(Sub):
    def draw(self):
        print("\tmy fourth programe")
        super().draw()

# main program
s1=Super()
s1.draw()

