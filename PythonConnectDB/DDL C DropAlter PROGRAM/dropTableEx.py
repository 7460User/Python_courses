import cx_Oracle
def droptable():
    try:
       con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
       cur=con.cursor()
       delete="drop table company  "
       cur.execute(delete)
       print("table removed/Dropt seccecfull----verify")
    except cx_Oracle.DataBaseError as db:
        print("prob in DB:",db)   

droptable()