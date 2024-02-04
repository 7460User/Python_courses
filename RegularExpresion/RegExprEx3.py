#RegExpr4.py
import re
gd="Python is an oop Lang. Python is  python also Fun Prog Lang"
sp="Python"
res=re.findall(sp,gd)  # here res is an object of list --res=['Python','Python']
print(res)
print("-------------------------------------------")
print(" '{}' found {} time(s)".format(sp,len(res)))