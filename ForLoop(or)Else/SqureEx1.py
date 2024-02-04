#Program for finding sum of Natural Nums, Squares and Cubes
#NatNumsSum.py
n=int(input("Enter How Many Natural Numbers Sum u want find:"))# 5
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-"*50)
	print("\tNat Nums\tSquares\tCubes")
	print("-"*50)
	i=1
	s,ss,cs=0,0,0
	while(i<=n):
		print("\t{}\t\t{}\t{}".format(i,i**2,i**3))
		i=i+1
		s=s+i
		ss=ss+i**2
		cs=cs+i**3
	else:
			print("-"*50)
			print("\t{}\t\t{}\t{}".format(s,ss,cs))
			print("-"*50)