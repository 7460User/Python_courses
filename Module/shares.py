#shares.py---file and treated as module name
def sharesinfo():
	d={"Tech":19,"Pharma":11,"Auto":1,"Finance":00}
	return d

#main program
#sharesdemo.py
import shares
import time
import importlib
def disp(d):
	print("-"*50)
	print("\tShare Name\tValue")
	print("-"*50)
	for sn,sv in d.items():
		print("\t{}\t\t:{}".format(sn,sv))
	else:
		print("-"*50)
#main program
d=shares.sharesinfo()  
disp(d)
time.sleep(15)
importlib.reload(shares)  # relodaing previously imported module
d=shares.sharesinfo() # obtaining changed / new values of previously  imported	module
disp(d)