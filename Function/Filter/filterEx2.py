posfun=lambda n:n>0
negfun=lambda n:n< 0
lst=[10,-28,49,-47,46,-59,-67,-68,90,+287,535,+5666] 
poslist=list(filter(posfun,lst))
neglist=tuple(filter(negfun,lst))
print("\nGiven your number={}".format(lst))
print("\nposstive list of Element:{}".format(poslist))
print("\nNegetive list of Element:{}".format(neglist))


