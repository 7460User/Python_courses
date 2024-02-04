import pickle
with open("E:/PY PROJECT/empinfo.data","ab")as fb:
    while(True):
        print("-"*50)
        eno=int(input("Enter employee number:"))
        ename=input("Enter employee name:")
        sal=float(input("enter employee salry:"))
        l=list()
   
        l.append(eno)
        l.append(ename)
        l.append(sal)
        pickle.dump(l,fb)
        print("Employee Data Saved Successfully File")
        print("-"*50)
        kl=input("Do you want insert another emp record (yes/no):")
        if (kl.lower()=="no"):
            break