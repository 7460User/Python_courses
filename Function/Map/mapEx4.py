#write a python program which will find squares of the positive numbers and square of negative numbers separately from given list of vals
#MapEx7.py
#main program
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split() if not val.isalpha()  ]
pnoslist=list(filter(lambda x: x>0,lst))
nnoslist=list(filter(lambda x: x<0,lst))
pnossqrlist=list(map(lambda k: k**2,pnoslist))
nnossqrlist=list(map(lambda k: k**2,nnoslist))
d1=dict(zip(pnoslist,pnossqrlist))
d2=dict(zip(nnoslist,nnossqrlist))
print("Possitive Numbers and their Squares:")
for n,sn in d1.items():
	print("\t{}-->{}".format(n,sn))
print("-"*50)
print("Negative Numbers and their Squares:")
for n,sn in d2.items():
	print("\t{}-->{}".format(n,sn))