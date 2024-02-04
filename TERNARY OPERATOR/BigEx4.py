#Program finding small and big among three Integer values.
#BigEx4.py
a=float(input("Enter Value of a:")) #10
b=float(input("Enter Value of b:")) #1
c=float(input("Enter Value of c:")) # 4
bv=a if b<a>c else  b if  a<b>c else c if a<c>=b else "ALL VALUES ARE EQUAL"
sv=a if   b>a<c else b if   a>b<c else c   if  a>c<=b else "All Values are Equal"
print("\nBig({},{},{})={}".format(a,b,c,bv))	
print("Small({},{},{})={}".format(a,b,c,sv))	
