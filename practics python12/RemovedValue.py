l1=[10,20,30,4,32,5,43,2,1,67,5,6,8,9]
x=int(input("Enter element to be removed:"))
if x in l1:
    l1.remove(x)
    print("Removed Successfully")
    print(l1)
else:
    print("Not a found element?")
