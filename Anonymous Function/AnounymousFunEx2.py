
big=lambda a,b: "Both value"if(a==b)else a if a>b else b
a,b=int(input("Enter Value a:")),int(input("Enter value of b:"))
gov=big(a,b)
print("big({},{})={}".format(a,b,gov))

