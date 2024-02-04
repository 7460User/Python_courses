#divop.py---File Name and Module name
from kvr import KvrDivisionError
def   division(a,b):
	if(b==0):
		raise KvrDivisionError # hitting or generating or raising  the exception
	else:
		c=a/b
		return c