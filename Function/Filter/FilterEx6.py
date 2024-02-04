#write a python program which will filter list of Even numbers
#FilterEx6.py
print("Enter List of Values separated by Space:")#  10  20  30 40 50 60 70 80
lst=[ int(val) for val in input().split() if int(val)>0 ]
print("Given List=",lst)
evenlist=list(filter(lambda n: n%2==0,lst))
print("Even List of Values:",evenlist)