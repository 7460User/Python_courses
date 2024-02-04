import cx_Oracle
def insertvalues():
   
    try:
         while(True):
            con=cx_Oracle.connect("system/tiger@localhost:1521/xe")
            cur=con.cursor()
            print("-"*50)
            id=int(input("Enter New Id:"))
            acno=int(input("Enter Account Number:"))
         
            cname=input("Enter your Name:")
            balence=float(input("Enter your balence:"))
            pin=int(input("Enter Your Pin:"))
           
            iq="insert into bankname values(%d,%d,'%s',%f,%d)"
            cur.execute(iq %(id,acno,cname,balence,pin))
            con.commit()
            print("insert your value seccesfull....verify")
            print("-"*50)
            ch=input("Do you want another insert(yes/no):")
            if (ch.lower()=="no"):
                break
    
    except cx_Oracle.dataBase as db:
        print("Your problem",db)
insertvalues()            
        
  
