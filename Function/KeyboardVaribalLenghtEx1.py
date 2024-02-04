def   dispinfo(**kvr):
	print("-"*50)
	print("Number of Keyword Variable Length values={}".format(len(kvr)))
	for k,v in kvr.items():
		print("\t{}-->{}--->{}".format(k,v))
	print("-"*50)

#main program
dispinfo(sno=10,sname="Rossum") # Function Call-1--kwd args
dispinfo(eno=1000,ename="Travis",sal=4.5) # Function Call-2--kwd args
dispinfo(tno=9999,tname="Rajesh",subject="Python", exp=10) # Function Call-3--kwd args
dispinfo(name="Ramesh",hobby1="Sleeping",hobby2="Eating",hobby3="Chatting")
dispinfo()