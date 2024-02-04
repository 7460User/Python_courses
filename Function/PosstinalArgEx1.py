#Program for demonstrating Posstional Arguments
#PossArgsEx1.py
def  dispstudinfo(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))



#main program
print("-"*50)
print("\tSno\tName\tMarks")
print("-"*50)
dispstudinfo(10,"Shiva",34.56) # Function Call
dispstudinfo(20,"Rock",44.56) # Function Call
dispstudinfo(30,"Khusb",34.66) # Function Call
dispstudinfo(40,"KVR ",11.66) # Function Call
dispstudinfo(50,"Imran ",26.66) # Function Call
print("-"*50)