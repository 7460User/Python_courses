n=int(input("Enter How Many Natural Number Sum U Want Find:"))
if(n<=0):
    print("{} is a invalid input".format(n))
else:
    print("-"*50)
    print("\tNat Numbs\tSquers\tCubes")
    print("-"*50)
    g,gg,cs=0,0,0
    for i in range(1,n+1):
        print("\t{}\t\t{}\t".format(i,i**2,i**3))
        g=g+i
        gg=gg+i**2
        cs=cs+i**3
        i=i+1
    else:
            print("-"*50)
            print("\t{}\t\t{}\t{}".format(g,gg,cs))
            print("-"*50)


         
            