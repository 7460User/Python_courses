import cx_Oracle
def  recordinsert():
    while True:
        try:
            con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
            cur=con.cursor()
            print("-"*30)
            empno=int(input("Enter Employee Number:"))
            ename=input("Enter Employee Name:")
            sal=float(input("Enter Employee salry:"))
            cname=input("Enter company name:")
            print("-"*50) 
            iq="insert into emp_tab values(%d,'%s',%f,'%s')"
            cur.execute(iq %(empno,ename,sal,cname))
            con.commit()
            print("cur data insrted")
            print("-"*50)
            ch=input("Do you want another insert(yes/no):")
            if (ch.lower()=="no"):
                break
            
        except cx_Oracle.DataBaseError:
            print("file not found error:")
recordinsert()            
