try:
    f=open("E:\\PY PROJECT\\pythonFileHandling\B.txt","w")
    f.write("Hello mr.subham\n and sukant\n you are luckey boy\n and subham tell me you full name:")
    # print(f.readline()) 
    # print(f.read(30))

except:
    print("File not found error....")
else:
    f.close()
    print("closed this file:")
    print("file created successfull.....")