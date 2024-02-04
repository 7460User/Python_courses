class student:
    def drawA(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        self.sloc=input("Enter Student Location:")
      
    def drawB(self):
        print("*"*30)
        print("\nStudent Details:")
        print("*"*30)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("Student Course:{}".format(self.crs))
        print("Student Location:{}".format(self.sloc))
        print("*"*30)
class main(student):
      def drawC(self):
        print("*"*50)
        print("Thankyou:")
        
        print("*"*50)
      
           
s=main()
s.drawA()
s.drawB()
s.drawC()





