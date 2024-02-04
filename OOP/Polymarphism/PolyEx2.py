class Circle:
    def draw(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        self.sloc=input("Enter Student Location:")
        print("*"*40)
        print("student Detail")
        print("*"*40)
        print("\t1.Student Number:{}".format(self.sno)) 
        print("\t2.Student Name:{}".format(self.sname))
        print("\t3.Student Course:{}".format(self.crs)) 
        print("\t4.Student  Location:{}".format(self.sloc))  
   
      
class Ract(Circle):
    def draw(self):
        print("*"*40)
        print("Welcome:")
        super().draw()
class emp(Ract):
    def draw(self):
        print("Hello BY")
        super().draw()
class table(emp):
    def draw(self):
        print("Hello Python")
        super().draw()                
     
r=table()
r.draw()               