#Program for deciding whether string is palindrome or not
#StringPalinEx2.py
s=input("Enter any Value:")
rs=s[::-1]
if(s==rs):
	print("Given String is Palindrome")
else:
	print("Given String is Not a Palindrome")