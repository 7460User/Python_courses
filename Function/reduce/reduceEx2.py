#write a python prog which will accept list of numerical vals and find max and min by using reduce functions
#reduceex3.py
import functools
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split() if not val.isalpha()]
#find max 
maxv=functools.reduce(lambda k,v: k if k>v else v, lst)  # [10,20,50,30,40] 
minv=functools.reduce(lambda k,v: k if k<v else v, lst)  # [10,20,50,30,40] 
print("\nMax({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))
