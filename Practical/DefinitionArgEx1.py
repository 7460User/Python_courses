def  dispstudinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t{}\t{}".format(sname,sno,marks,crs))


print("-"*50)
print("\tName\tsno\tMarks\tcrs")
print("-"*50)
dispstudinfo("pooja",1,37.60,crs="java")  
dispstudinfo("rima",2,69.50,crs="pyhton")    
dispstudinfo("sonu",3,99.10,crs="Angular")      
print("-"*50)