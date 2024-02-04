#Program finding small and big among three Integer values.
#BigEx3.py
a=float(input("Enter Value of a:")) # 10
b=float(input("Enter Value of b:")) #10
c=float(input("Enter Value of c:")) # 10
#Find Big and small
big=a if (a>b) and (a>c) else b  if(b>a) and (b>c)  else c  if (c>a) and (c>=b) else "ALL ARE EQUAL"
small=a if (a<b) and (a<c) else b if (b<a) and (b<c) else c if (c<a) and (c<=b)  else "THREE VALUES ARE EQUAL"

print("\nBig({},{},{})={}".format(a,b,c,big))
print("Samll({},{},{})={}".format(a,b,c,small))
