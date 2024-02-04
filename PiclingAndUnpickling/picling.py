import pickle

# picling a python object
try:
    csr=["car","Suzuki","VMW","mahendra","tata","mrf",123]

    fileobj =open("E:\\PY PROJECT\\PiclingAndUnpickling\A.pkl",'wb')
    pickle.dump(csr,fileobj)
except:
    print("file is not found:")

else:
    print("file is converted bytcode successufully....")
    

fileobj.close()