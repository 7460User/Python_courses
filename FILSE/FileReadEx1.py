#FileReadEx1.py
try:
	filename=input("Enter Any File Name:")
	with open(filename,"r") as fp:
		filedata=fp.read()
		print("-"*50)
		print(filedata)
		print("-"*50)
except FileNotFoundError:
	print("File does not exist")
