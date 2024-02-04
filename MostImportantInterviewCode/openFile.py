# f=open('abc.txt','r')
# data=f.read()
# print(data)
# f.close()
data="hello mr govind kumar maurya:"
f=open('abc.txt','w')
f.write(data)
with open('abc.txt','r+')as f:
    text=f.read()
    print(text)