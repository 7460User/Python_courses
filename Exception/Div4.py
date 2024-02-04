
try:
    print("Exception started")
    s1=input("Enter your number:")
    s2=input("enter your second value:")
    a=float(s1)
    b=float(s2)
    c=a/b
except ZeroDivisionError:
    print("\tInput is wrong?")
except ValueError:
    print("\tThis is Not Accept Any Symbole:")  
else: 
    print("="*50)     
    print("value of a=",a)
    print("value of b=",b)
    print("Div=",c)
    print("="*50)
finally:
    print("Finly block equestion")    
