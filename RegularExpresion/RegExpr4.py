import re
res=re.finditer("k","kkvkvkkkkvkvr")
print("-"*40)
for mat in res:
    print("start index:{}End index:{} value:{}".format(mat.start(),mat.end(),mat.group()))
    print("-"*40)