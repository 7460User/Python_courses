def multable(n):
    if(n<=0):
        print("Invalid number")
    else:
        print("-"*50)
        print("print sum table")
        for i in range(1,11):
          print("sum:({}X{})={}".format(n,i,n*i)) 
        print("-"*50) 
def addit(n):
    print("-"*50)
    print("add a total value")
    for i in range(n+1):
        print("add value:({}+{})={}".format(n,i,n+i))
        print("-"*50)
        
