#HighestpalindromeEx2.py
lst=["MOM","DAD","LIRIL","MADAM","MALAYALAM","Python","RACECAR"]
hpl=0
ind= -1
for i in range(0,len(lst)):
	cl=0
	cv=str(lst[i])
	if(cv==cv[::-1]):
		cl=len(cv)
		
	if(cl>hpl):
		hpl=cl
		ind=i	
print("Higheest palindrome ={}".format(lst[ind]))
print("{}  whose length is  {}".format(lst[ind], hpl))