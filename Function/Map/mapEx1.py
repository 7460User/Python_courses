def hike (sal):
    sal=sal+sal*(20/100)
    return sal
oldsallist=[23,34,43,37,78] 
m=map(hike,oldsallist)
print("type of m=",type(m))
print("content of m=",m)       
print("-"*50)
newsallist=list(m)
print("\nold sal list=",oldsallist)
print("\nNew sal list=",newsallist)