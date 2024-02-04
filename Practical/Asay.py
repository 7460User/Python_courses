big=lambda a,b:"both of value" if(a==b) else a if a>b else b
a,b=int(input("Enter value of a:")),int(input("Enter value of b:"))
gb=big(a,b)
print("big({},{})={}".format(a,b,gb))