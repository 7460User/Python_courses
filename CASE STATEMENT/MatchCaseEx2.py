#Program for implementing AOP Operation by using match case with menu driven Procedure
#MatchCaseEx2.py
import sys
print("-"*50)
print("\tArithmetic Operations")
print("-"*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Div")
print("\t6.Exponentiation")
print("\t7.Exit")
print("-"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
	
	case 1:
		a=float(input("Enter First value for Addition:"))
		b=float(input("Enter Second value for Addition:"))
		print("sum({},{})={}".format(a,b,a+b))
	case 2: 
		a=float(input("Enter First value for Sub:"))
		b=float(input("Enter Second value for Sub:"))
		print("sub({},{})={}".format(a,b,a-b))
	case 3:
		a=float(input("Enter First value for Mul:"))
		b=float(input("Enter Second value for Mul:"))
		print("Mul({},{})={}".format(a,b,a*b))
	case 4:
		a=float(input("Enter First value for Div:"))
		b=float(input("Enter Second value for Div:"))
		print("Div({},{})={}".format(a,b,a/b))
		print("F.Div({},{})={}".format(a,b,a//b))
	case 5:
		a=float(input("Enter First value for Mod Div:"))
		b=float(input("Enter Second value for Mod Div :"))
		print("Mod({},{})={}".format(a,b,a%b))
	case 6:
		a=float(input("Enter Base:"))
		b=float(input("Enter Power:"))
		print("Pow({},{})={}".format(a,b,a**b))
	case 7:
		print("Thx for using this Program")
		sys.exit()  # exit() is used for Physical termination of the program
	case _: # default case block
		print("Ur Selection of Operation is wrong:")	

print("Other statements")
		
