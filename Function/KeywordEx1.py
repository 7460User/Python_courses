#Program for demonstrating Keyword Arguments
#KeyWordArgsEx1.py
def   disp(a,b,c):
	print("\t{}\t{}\t{}".format(a,b,c))

#main program
print("-"*50)
print("\tA\tB\tC")
print("-"*50)
disp(10,20,30) # Possitional Args
disp(a=30,c=10,b=20) # Key Word Args
disp(b=20,c=30,a=10) # Key Word Args
disp(c=30,b=20,a=10) # Key Word Args
disp(10,c=30,b=20) # Possitional and Key Word Args
disp(b=100,c=200,a=300) # Possitional and Key Word Args

print("-"*50)