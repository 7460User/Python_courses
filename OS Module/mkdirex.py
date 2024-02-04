import os
try:
    os.mkdir("E:\PY PROJECT\OS Module/google/govind")
    print("Folder created succesfully-verify")
except FileNotFoundError:
    print("the specified folder already exit") 
except FileNotFoundError:
    print("mkdir()can create only one  folder at time")
except OSError:
    print("check your path of folder names")    
