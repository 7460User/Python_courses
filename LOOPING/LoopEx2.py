from re import I


n=int(input("Enter a number:"))
if(n<=0):
    print("{} :invalid Input".format(n))
else:
    i=1
while(i<=n):
    print("while loop-->\t{}".format(i))
    i=i+1
    print("down print")
    

