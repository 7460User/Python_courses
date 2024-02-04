try:
    srcfilename=input("Enter Any File Name:")
    with open(srcfilename,"r")as fb:
        dstfile=input("Enter DSestination File:")
        with open(dstfile,"a")as gk:
            srcfilenamedata=fb.read()
            gk.write(srcfilenamedata)
            print("Source file data compied into dest file")
except FileNotFoundError:
    print("file Does Not exist")        
