try:
    filename=input("Enter File Name:")
    nl,nw,nc=0,0,0
    with open(filename,"r") as fb:
        lines=fb.readlines()
        for line in lines:
            nl=nl+1
            nw=nw+len(line.split())
            nc=nc+len(line)
        else:
            print("Number of Lines=",nl)
            print("Num of words=",nw) 
            print("Numbers of chars=",nc)   
except FileNotFoundError:
    print("File does not exist")
    
