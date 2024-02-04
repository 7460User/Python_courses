import cx_Oracle
def newtable():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        itable="create table bankname(id number(3),acno number(10),cname varchar(20),balence float(50),pin number(4))"
        cur.execute(itable)
        print("created table seccesfull..")
    except cx_Oracle.DataBaseError as db:
        print("problrm",db)
newtable()            

        