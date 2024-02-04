#Program for demonstrating Variable  length arguments
#PureVarAgrsEx5.py
def    findsum(sno,sname, *a,crs="PYTHON"):
	print("-"*50)
	print("Number of Values:{}".format(len(a)))
	print("Student Number:{} and Name:{}".format(sno,sname))
	print("Learning '{}' Course:".format(crs))
	s=0
	for val in a:
		s=s+val
		print("{}".format(val),end=" ")
	print()
	print("Sum={}".format(s))
	print("-"*50)
#main program
findsum(10,"Rossum",10,20,30,40,50)
findsum(20,"Travis",10,20,30,40)
findsum(30,"Ritche",10,20,30)
findsum(40,"Kinney",10,20)
findsum(50,"Jango",10)
findsum(60,"James")
#findsum(70,"Kvr",-2,-3,"JAVA")---error
findsum(70,"Kvr",-2,-3,crs="JAVA")
#findsum(crs="R",-10,-20,-30,sname="Rajesh",sno=80)-------error
#findsum(70,"Kvr",crs="JAVA",-2,-3)---SyntaxError: positional argument follows keyword argument