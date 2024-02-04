#write a python program which will read employee recods
#fetchall()-----list of tuples
#SelectRecordsEx3.py
import cx_Oracle
def  selectrecords():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        cur.execute("select * from emp_table")
        print("-" * 50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val),end=" ")
            print()
        print("-" * 50)
    except cx_Oracle.DatabaseError as db:
        print("Prob in Database:",db)

#main program
selectrecords()                    

