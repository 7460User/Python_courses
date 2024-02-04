#Program for accepting two integer values and find their div
#Div2.pyprint("try --program Execution started:")
try:
   s1=input("Enter First Value:")
   s2=input("Enter Second Value:")
   a=int(s1)
   b=int(s2)
   c=a/b
   print("\n do not enter for DEN..")
except ValueError:
   print("/ndon't enteger starts A muns and symbols")   
   print("value of a=",a)
   print("value of b=",b)
   print("div c=",c)
   print("\tnfinally block --program excution ended:")

