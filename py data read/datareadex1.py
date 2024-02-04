print("Enter First Value:")
s1=input()
print(s1,type(s1))
print("Enter Second Value:")
s2=input()
print(s2,type(s2))
#Type cast s1 and s2 into float 
a=float(s1)
b=float(s2)
c=a*b
print("mul({},{})={}".format(a,b,c))
print("---------OR-------------------")
print("mul(%0.2f,%0.2f)=%0.2f" %(a,b,c))
