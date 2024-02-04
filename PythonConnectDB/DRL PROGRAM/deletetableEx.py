import cx_Oracle
def deletevalue():
    try:
            con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
            cur=con.cursor()
            #accept the data from KBD
            print("-"*50)
            id=int(input("Enter Your Id:"))
            print("-" * 50)
            #prepare the query and execute
            iq="delete from bankname where id=%d"
            cur.execute(iq %id)
            #OR
            #cur.execute("delete from employee where enp=%d" %empno")
            con.commit()
            if(cur.rowcount>0):
                print("Employee Record Removed Successfully")
            else:
                print("Employee Record does not exist")
            print("-" * 50)
            ch=input("Do u want to delete record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using Program")
    
    except cx_Oracle.BataBaseError as db:
        print("problem is ",db)
deletevalue()            
