#write a python program for getting col names
#ColNamesEx2.py
import cx_Oracle
def  selectcolnames():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        cur.execute("select * from emp_table")
        #get Col Names
        print("-" * 50)
        for colname in [tabinfo[0] for tabinfo in cur.description]:
            print("\t{}".format(colname),end=" ")
        print()
        print("-"*50)
        #display records
        records = cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val), end=" ")
            print()
        print("-" * 50)
    except cx_Oracle.DatabaseError as db:
        print("Prob in Database:",db)

#main program
selectcolnames()