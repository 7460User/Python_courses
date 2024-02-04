#program deleting the record
#RecordDeleteEx2.py
import cx_Oracle
def deleterecord():
    while(True):
        try:
            con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
            cur=con.cursor()
            #accept emp number from KBD
            empno=int(input("Enter Employee Number:"))
            #prepare query and executre
            dq="delete from emp_table where empno=%d "
            cur.execute(dq %empno)
            con.commit()
            if(cur.rowcount>0):
                print("Record Deleted Sucessfully")
            else:
                print("Record does not exist")
            ch=input("Do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                break
        except cx_Oracle.DatabaseError as db:
            print("Prob in Database:",db)

#main program
deleterecord()