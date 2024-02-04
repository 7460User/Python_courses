import cx_Oracle
def columnname():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        cur.execute("select * from emp_table")
        print("-"*50)
        tabdes=cur.description
        print("-"*50)
        for tabinfo in tabdes:
            print("\t{}".format(tabinfo[0]),end="")
        print()
        print("-"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val),end="")
            print()
            print("-"*50)
    except cx_Oracle.DataBaseError as db:
        print("problem",db)
columnname()        
                



