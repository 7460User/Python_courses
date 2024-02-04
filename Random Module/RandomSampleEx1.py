#Program for generating Number plaate values
#Syntax:   random.sample()
#RandomSampleEx1.py
import random as r
dgs="0123456789"
alpha="ABCDEFGHIJKLMONOPQRSTUVWXYZ"
for i in range(1,11):
	x=r.sample(dgs,4)
	np=""
	for num in x:
		np=np+str(num)
	y=r.sample(alpha,2)
	na=""
	for al in y:
		na=na+al
	print("TS09"+na+np)