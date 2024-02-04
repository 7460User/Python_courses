sum=int(input("Enter Any Number:"))
if(sum<=0):
   
    print("{} is Invalid Number".format(sum))

else:
     print("-"*50)
     i=1
     while(i<=10):
        print("\t{}*{}={}".format(sum,i,sum*i))
        i=i+1
     else:
         print("-"*50)

