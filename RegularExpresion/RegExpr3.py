import re
bd="python is an oop lang.python is also fun program lang"
sp="python"
res=re.search(sp,bd)
if(res!=None):
    print("Start index:{}".format(res.start()))
    print("End index:{}".format(res.end()))
    print("Matched Value:{}".format(res.group()))
    print("Search is Successfull")
else:
    print("Search is un-successfull")
