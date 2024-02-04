def multitable(n):
    if(n<=0):
        print("({})invalid input ".format(n))
    else:
        print("-"*50)
       
        print("-"*50)
        for i in range(1,11):
            print("\t{} * {} = {}".format(n,i,n*i))
         
n=int(input("Enter Any Value:"))
multitable(n)

