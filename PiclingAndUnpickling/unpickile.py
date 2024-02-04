import pickle

# unpicling to python object

file="A"
fileobje=open("E:\\PY PROJECT\\PiclingAndUnpickling\A.pkl",'rb')
A=pickle.load(fileobje)
print(A)
print(A,type(A))