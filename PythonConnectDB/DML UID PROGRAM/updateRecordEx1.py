import cx_Oracle
def updaterecord():
    try:
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        up="update emp_table set(empno=25,ename='veer',sal=2.3,cname='jaira' )where empno=10"
        cur.execute(up)
        print("Your table is a updated seccesfull....")
    except cx_Oracle.DataBaseError as k:    

        print("Module not fund error:")    
updaterecord()    