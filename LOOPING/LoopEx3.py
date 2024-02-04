from tkinter import N


g=int(input("Enter a number:"))
if(g<=0):
    print("{} in this not correct".format(g))
else:
    print("-"*50)
    print("Numbers Within:{}:".format(g))
    i=g
    while(i>0):
        print("\t{}".format(g))
        i=i-1
        print("-"*50)
