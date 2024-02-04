import cx_Oracle
def insertvalue():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        iq="insert into emp_table values(10,'jain',2.3,'lenov')"
        cur.execute(iq)
        con.commit()
        print("values add seccesfull---")
    except cx_Oracle.DataBase as k:
        print("Module not found error")
insertvalue()
