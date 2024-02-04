import cx_Oracle
def newtable():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        itable="create table emp_tab(empno number(20),ename varchar(20),salary float(50),cname varchar(40))"
        cur.execute(itable)
        print("created table seccesfull..")
    except cx_Oracle.DataBaseError as db:
        print("problrm",db)
newtable()  