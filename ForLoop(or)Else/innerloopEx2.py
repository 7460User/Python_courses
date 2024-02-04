#InnerLoopEx2.py
i=1
while(i<=5):
	print("-"*50)
	print("Outer while Loop--Val of i :{}".format(i))
	j=1
	while(j<=3):
		print("\tInner while Loop--Val of j :{}".format(j))
		j=j+1
	else:
		i=i+1
		print("i am coming out-of inner while loop")
else:
	print("i am coming out-of outer while loop")
	print("-"*50)
