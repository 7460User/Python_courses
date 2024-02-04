#AnounymousFunEx3.py

big=lambda a,b,c: a if (b<=a>c) else b if (a<b>=c) else c if (a<c>b) else "All Values are equal:"
small=lambda a,b,c: a if (b>a<c) else b if (a>b<=c) else c if (a>c<b) else "All Values are equal:"

#main program
a,b,c=int(input("Enter Value of a:")),int(input("Enter Value of b:")),int(input("Enter Value of c:"))
bv=big(a,b,c)
sv=small(a,b,c)
print("big({},{},{})={}".format(a,b,c,bv))
print("small({},{},{})={}".format(a,b,c,sv))
