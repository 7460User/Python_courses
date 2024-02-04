
def mulof(n):
    if(n<=0):
        print("Invalid input")
    else:    
        print("-"*50)
        i=1
        for i in range(10,19):
       
            print("multitable({}X{})={}".format(n,i,n*i))
            i=i+1
