import cx_Oracle
try:
    def cursor():
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        k=con.cursor()
        print("\ncursor oblect created")
        print("Type of k=",type(k))
except cx_Oracle.DataBaseError as d:
    print("problram in DB:",d)
cursor()     
