even=lambda n:(n%2==0) and (n>0)
lst=[10,-29,-36,48,-56,-58,-78]
evenlist=list(filter(even,lst))
print("\nGiven Element number:{}".format(lst))
print("\nThis is your even number:{}".format(evenlist))


