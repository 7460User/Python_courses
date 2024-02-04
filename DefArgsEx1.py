#Program for demonstrating Default Arguments
#DefArgsEx1.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))



#main program
print("-"*50)
print("\tSno\tName\tMarks\tCrs")
print("-"*50)
dispstudinfo(10,"Shiva",34.56) # Function Call
dispstudinfo(20,"Rock",44.56) # Function Call
dispstudinfo(30,"Khusb",34.66) # Function Call
dispstudinfo(40,"KVR ",11.66) # Function Call
dispstudinfo(50,"Imran ",26.66) # Function Call
dispstudinfo(60,"Ganesh ",16.66,"JAVA") # Function Call
dispstudinfo(70,"Rajesh ",26.66) # Function Call

print("-"*50)   
