#Program for demonstrating for loop in for loop
#InnerLoopEx3.py
for i in range(5,0,-1):
	print("-"*50)
	print("Outer for Loop--Val of i :{}".format(i))
	j=1
	while(j<=3):
		print("\tInner while Loop--Val of j :{}".format(j))
		j=j+1
	else:
		i=i+1
		print("i am coming out-of inner while loop")
else:
	print("i am coming out-of outer for loop")
	print("-"*50)