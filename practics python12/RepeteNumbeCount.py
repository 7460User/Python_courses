words=input("Enter some words:")
d={}
for x in words:
    d[x]=d.get(x,0)+1
    for k,v in d.items():
        print("{} occured {} times".format(k,v))
