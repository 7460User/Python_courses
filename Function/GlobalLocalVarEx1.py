#GlobalLocalVarEx1.py
lang="PYTHON" # Global Variable
def   learnDS():
	sub1="DS" # Local Variable
	print("\nTo develop '{}' application, we use '{}' Programming".format(sub1,lang))
	#print(sub2,sub3)--> we can't access sub2 and sub3 in current function bcoz they are local to other functions

def   learnAI():
	sub2="AI" # Local Variable
	print("\nTo develop '{}' application, we use '{}' Programming".format(sub2,lang))
	#print(sub1,sub3)--> we can't access sub1 and sub3 in current function bcoz they are local to other functions

def   learnIOT():
	sub3="IOT" # Local Variable
	print("\nTo develop '{}' application, we use '{}' Programming".format(sub3,lang))
	#print(sub1,sub2)--> we can't access sub1 and sub2 in current function bcoz they are local to other functions

#main program
learnDS()
learnAI()
learnIOT()