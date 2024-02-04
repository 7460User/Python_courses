#Who is biggest Value
#BigEx2.py


a=float(input("Enter value of A:"))
b=float(input("Enter Value of B:"))
res=a if a>b else b if b>a else "Both Number Equel"
print("big({},{})={}".format(a,b,res))
