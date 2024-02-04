
#program for creating a table
#TableCreateEx.py
import cx_Oracle
def createtable():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        #prepare the query and execute
        tq="create table company(tno number(2) primary key, tname varchar2(10),sub varchar2(10))"
        cur.execute(tq)
        print("Table Created Successfully---Verify")
    except cx_Oracle.DatabaseError as db:
        print("Prob in DB:",db)

#main program
createtable()