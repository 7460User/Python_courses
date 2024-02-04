#program for demonstarting globals() 
#globalsfunex2.py
a=10
b=20  # Here 'a' and 'b' are called global variables
def   getinformation():
	d=globals()  #   d ={ implicit global varibles,   a:10, b:20}
	for k,v in d.items():
		print("\t{}---->{}".format(k,v))
	print("-"*50)
	print("Programmer-defined globval Var--Way1:")
	print("-"*50)
	print("Val of GV a:{}".format(d['a']))
	print("Val of GV b:{}".format(d['b']))
	print("-"*50)
	print("Programmer-defined global Var--Way2:")
	print("-"*50)
	print("Val of GV a:{}".format(d.get('a')))
	print("Val of GV b:{}".format(d.get('b')))
	print("-"*50)
	print("Programmer-defined global Var--Way3:")
	print("-"*50)
	print("Val of GV a:{}".format(globals()['a']))
	print("Val of GV b:{}".format(globals()['b']))
	print("-"*50)
	print("Programmer-defined global Var--Way4:")
	print("-"*50)
	print("Val of GV a:{}".format(globals().get('a')))
	print("Val of GV b:{}".format(globals().get('b')))
	print("-"*50)





#main program

getinformation()
	