#Program accepting a word and decides whether the First and Last Characters is same or not
#FistLastCharEx1.py
word=input("Enter Word:")  # Word   :     DAD    RUBBER   
res="First and Last Chars are Same"  if word[0]==word[-1] else "First and Last Chars are Different"
print("result=",res)
