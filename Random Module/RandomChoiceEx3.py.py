#Program for generating choice of values from given str
#Syntax:   random.choice()
#RandomChoiceEx3.py
import random as r
s1="ABCDEFGHIJabcdefghijklmnopqrstuvwxyzKLMONOPQRSTUVWXYZ"
s2="0123456789"
s3="~!@#$%^&*()_+"
for i in range(4,9):
	print(r.choice(s1),r.choice(s2),r.choice(s3),r.choice(s1))