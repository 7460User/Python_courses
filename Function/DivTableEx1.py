def divtable(n):
    if(n<=0):
        print("{} Invalid Input".format)
    else:
        for i in range(2,11):
            print("\t({}/{})={}".format(n,i,n/i))
n=int(input("Enter Any Value:"))
divtable(n)            
