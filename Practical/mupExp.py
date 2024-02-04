
from tkinter import N


n=int(input("Enter Any Number:"))
if(n<=0):
    print("{} Invalid Input".format(n))
else:
    i=0
    while(i<=10):
        print("{}*{}={}".format(n,i,n*i))
        i=i+1
       
  
 
