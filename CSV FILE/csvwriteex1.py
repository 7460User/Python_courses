#csvwriteex1.py
#field / header names
import csv
recfields=['Name','Branch','year','CGPA']
#data row of csv files 
rows=[['Nikkil','CSE','2','9.0'],
      ['sachin','CSE','2','9.1'],
      ['bikki','IT','3','12.32'],
      ['pankaj','NonIT','2','5.4'],
      ['rahul','it','3','3.4'],
      ['RaviLanth','MCA','2','80.0']],
#name of csv file
csvfilename="univ1.csv"
#writing data to csv file
with open (csvfilename,'w')as fp:
    #creating a csv writer object
    csvwriter = csv.writer(fp)
    #writer the fields /header name
    csvwriter.writerow(recfields)
    #writing the data rows 
    csvwriter.writerows(rows)
    print("\nCSV file Created  and Verify")


