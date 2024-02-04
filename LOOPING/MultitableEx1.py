#NumGenEx1.py
n=int(input("Enter a Number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    i=1  # Initlixzation Part
    while(i<=n):  # i<=m is called Cond
        print("\t{}".format(i),end=' ')
        i=i+1 # Updation Part