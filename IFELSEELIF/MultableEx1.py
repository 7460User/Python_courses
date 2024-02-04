n=int(input("Enter a number for generating Mul Table:"))
if(n<=0):
    print("{} is invalid number".format(n))
else:
    print("="*50)
    print("Mul Table for: {}".format(n))
    print("="*50)
    i=1
    while(i<=10):
        print("\t{}*{}={}".format(n,i,n*i))
        i=i+1
    else:
        print("="*50)

