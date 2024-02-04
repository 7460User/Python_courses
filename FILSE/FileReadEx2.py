try:
    filename=input("Enter Any File Name")
    with open(filename,"r")as fb:
        lines=fb.readlines()
        print("-"*50)
        print(lines,end="r")
        print("-"*50)
except FileNotFoundError:
    print("File Not Found")
