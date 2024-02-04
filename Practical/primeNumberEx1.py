sum=int(input("Enter Any Number:"))
if(sum<=1):
    print("Invalid Number {}".format(sum))
else:
    while(sum%2==0):
        print("odd Number{}".format(sum))
    else:
        print("{}Prime Number".format(sum))
