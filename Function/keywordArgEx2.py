#Program for demonstrating Keyword Arguments
#KeyWordArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))



print("-"*50)
print("\tSno\tName\tMarks\tCrs\tCountry")
print("-"*50)
dispstudinfo(10,"RS",11.11) # Possitional Args
dispstudinfo(marks=22.22,sno=20,sname="TR",crs="UI") # Keyword Args 
dispstudinfo(cnt="USA",sname="Trump",crs="Poli",marks=6.66,sno=40)
dispstudinfo(10,"DR",cnt="UK",marks=34.56,crs="JAVA")
print("-"*50)