#program for reading records from file by using unpickling
#empunpickex1.py--Program-(B)
import pickle
try:
    with open("E:/py project/empinfo.data","rb") as fp:
        print("="*50)
        while(True):
            try:
                objdata = pickle.load(fp)
                for val in objdata:
                    print("\t{}".format(val),end="")
                print()
            except EOFError:
                print("="*50)
                break
except FileNotFoundError:
    print("File does not exist")