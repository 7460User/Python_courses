def printof(n):
    if(n<=0):
        print("Invalid input number")
    else:    
        print("This is factorial number")
        f=1
        for i in range(1,n+1):
            f=f*i
            print("factorial:{}".format(n,i,n*i))
