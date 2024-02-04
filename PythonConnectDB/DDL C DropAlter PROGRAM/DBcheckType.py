import cx_Oracle
def connection():
    con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
    print("python obtains oracle data base")
    print("type of con=",type(con))
connection()    
