# Python program to demonstrate to write single record
#csvwriteex2.py
import csv
row=['Aryan','CSE','2','9.4']
filename="univ1.csv"
with open(filename,"a")as fp:
    ch=csv.writer(fp)
    ch.writerow(row)
    print("\nSingle Record Written to the csv file:")