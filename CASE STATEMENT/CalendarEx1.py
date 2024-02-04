#Program for display ing the month calendar for year and month name
#CalendarEx1.py
import calendar
mons={"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}
year=int(input("Enter Year Number:")) # 2022
month1=input("Enter Month Name:")  # Oct
if(year<=0) or (mons.get(month1[0:3])==None):
	print("Invalid details")
else:
	print(calendar.month(year,mons.get(month1[0:3].upper() ) ))