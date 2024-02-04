from audioop import mul


s=int(input("Enter Any Number:"))#10
if(s<=0):
    print("{} is Not Accept Value".format(s))
else:
    i=1
    while(i<=10):
        print("\t{}*{}={}".format(s,i,s*i))
        i=i+1

    