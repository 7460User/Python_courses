#Program for demonstrating Local and Global variables and their values
#GlobalLocalVarEx5.py
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
#lang="PYTHON" # Global Variable---we can't access in learnDS(), learnAI() and learnIOT() bcoz we defined lang as global varaibles after function calls.