#Program for cal Arithmetic Operations By using Assigment Operator
#MultiLineAop.py
a,b=int(input("Enter Value of a:")), int(input("Enter Value of b:"))
sum,sub,mul,div,fdiv,mod,exp=a+b,a-b,a*b,a/b,a//b,a%b,a**b
print("-"*50)
print("\tArithmetic Operators ")
print("-"*50)
print("\tsum({},{})={}".format(a,b,sum))
print("\tsub({},{})={}".format(a,b,sub))
print("\tmul({},{})={}".format(a,b,mul))
print("\tdiv({},{})={}".format(a,b,div))
print("\tF.Div({},{})={}".format(a,b,fdiv))
print("\tmod({},{})={}".format(a,b,mod))
print("\tpow({},{})={}".format(a,b,exp))
print("-"*50)
