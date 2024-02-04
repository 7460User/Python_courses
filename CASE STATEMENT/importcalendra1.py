import calendar
year=int(input("Enter the year:"))
mont=input("Enter the month name:")
a={"january":1,"febuary":2,"march":3,"april":4,"may":5,"jun":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
for i in a:
    if mont.lower() in i:
        print(calendar.month(year, a.get(i)))
        exit()
print("Enter the correct month name")
