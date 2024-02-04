print("Enter First list of element:")
lst1=[int(val)for val in input().split()]
print("Enter Second of element:")
lst2=[int(val)for val in input().split()]
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("first list element:",lst1)
print("second list element:",lst2)

