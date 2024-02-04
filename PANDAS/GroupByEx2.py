import pandas as pd
employee =[ 
                      (11,'jack',44, 'mumbai',  19),
           (12,'sohan',38, 'sonebh', 10),
           (13,'mohan',40, 'hyd',  11),
           (14,'gulabo',34, 'delhi',  14),
           (15,'rausan',64, 'mumbai', 13),
           (16,'puspa',30, 'delhi', 18),
           (17,'raaunak',23, 'hyd', 16),
           (18,'pujara',36, 'gujrat',19),
           (19,'golua',28, 'delhi', 11),
           (20,'raju',44, 'mumbai',  14)]
df=pd.DataFrame(employee,columns=['ID','Name','Age','city','Experince'])
df=df.set_index('ID')
print("-"*50)
print(df)
print("-"*50) 
print("---------------------------------")
groupObj=df.groupby('city')
for grpName, rows in groupObj:
    print("Group Name: ", grpName)
    print('Group Content: ')
    print(rows)          
    print("---------------------------------")