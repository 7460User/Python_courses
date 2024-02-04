from tkinter import N


s="PYTHON"
print("for loop without break statm .............")
for ch in s:
    print("{}".format(ch))
else:
    print("I am from else --part ---0f----for loop")
    #Display PYT
    for v in s:
        if (v=="H"):
            break
        else:
            print("{}".format(v))
    else:
        print("I am from else --part ---0f----for loop")
        print("Other Statements in program")

