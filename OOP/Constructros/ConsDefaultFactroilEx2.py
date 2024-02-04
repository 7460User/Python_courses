class Factorial:
    def __init__(self):
        print("*"*50)
        self.n=int(input("Enter Any Number:"))
    def callfact(self):
        if(self.n<=0):
            print("invalid input".format(self.n))
        else:
         f=1
         for i in range(1,self.n+1):
            f=f*i
         else:
            print("*"*50)
            print("Foctorial({})={}".format(self.n,f))
            print("*"*50)

t1=Factorial()
t1.callfact()            


       
            
         

        