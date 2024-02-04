#Program for deciding whether Given word is Palindrome or not
# HINT----->  LIRIL   RACECAR     MALAYALAM  MADAM   MOM DAD.....etc of Palindromes
#WordPlainromeEx1.py
word=input("Enter a word:") # PYTHON
res="PALINDROME"   if word==word[::-1] else "NOT PALINDROME"
print("{} is {}".format(word,res))
