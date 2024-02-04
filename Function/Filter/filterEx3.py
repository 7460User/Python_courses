posstive=lambda b:b>0
nagetive=lambda b:b<0
lst=[-3,-4,-5,-10,-40,-60,-70]
posstivelist=list(filter(posstive,lst))
nagetivelist=tuple(filter(nagetive,lst))
print("\tGiven your number:{}".format(lst))
print("\tThis is posstive number:{}".format(posstivelist))
print("\tTnis is nagetive number:{}".format(nagetivelist))
