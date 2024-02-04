import os

if os.path.exists("E:\\PY PROJECT\\pythonFileHandling\B.txt"):
    os.remove("E:\\PY PROJECT\\pythonFileHandling\B.txt")

    print("file deleted succesfully...")        
else:
    
    print("file not found error:")    