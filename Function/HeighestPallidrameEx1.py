#write a python prog which will extract highest pallendrim among list of pallendrim
# HINT:  [ 1  121  5454545  , 90909, 8558]
#HighestpalindromeEx1.py
lst=[ 1, 121,5455  , 90909, 8558,888888888888]
strt=0
end= -1
for i in range(0,len(lst)):
	cl=0
	cv=str(lst[i])
	if(cv==cv[::-1]):
		cl=len(cv)
		
	if(cl>strt):
		strt=cl
		end=i	
print("Higheest palindrome ={}".format(lst[end]))
print("{}  whose length is  {}".format(lst[end], strt))