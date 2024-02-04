
age=int(input("Enter Your Age:"))
if(age>=18)and(age<=90):
    
    print("="*50)
    print("\tYou Are eligible for give Vote:".format(age))
    print("="*50)
else:
     
    print("\tYou Are Not Eligible For Give Votes:".format(age))
    print("="*50)