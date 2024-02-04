import cx_Oracle,sys
class Employee:
 
    def reademployeevalues(self):
        print("*"*50)
        self.eno=int(input("Enter employee Number:"))
        self.ename=(input("Enter Employee Name:"))
        self.sal=float(input("Employee salary:"))
        self.cname=(input("Enter  company Name:"))
        print("*"*50)
    def DBstoredata(self):
        con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
        cur=con.cursor()
        cur.execute("insert into employeee values(%d,'%s',%f,'%s')" %(self.eno,self.ename,self.sal,self.cname))
        con.commit()
        print("{} record your complete".format(cur))
try:
    s=Employee()
    s.reademployeevalues()
    s.DBstoredata()
except cx_Oracle.DatabaseError as db:
    print("Problem in Database:", db)
except ValueError:
    print("Don't enter alnums, sts and symbols for empno and sal")





