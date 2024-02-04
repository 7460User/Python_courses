#Program for demonstrating Posstional Arguments
#PossArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))



#main program
print("-"*50)
print("\tSno\tName\tMarks\tCrs")
print("-"*50)
dispstudinfo(10,"Shiva",34.56,"PYTHON") # Function Call
dispstudinfo(20,"Rock",44.56,crs="AWS") # Function Call
dispstudinfo(30,"Khusb",34.66,"PYTHON") # Function Call
dispstudinfo(40,"KVR ",11.66,crs="UI Development") # Function Call
dispstudinfo(50,"Imran ",26.66,crs="Java") # Function Call
print("-"*50)