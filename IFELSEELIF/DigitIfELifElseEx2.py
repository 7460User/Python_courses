#Program for accepting the digit and print its name 
#DigitIfELifElseEx4.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
dig=int(input("Enter Any Digit:")) 
res=  d.get(dig) if d.get(dig)!=None  else "Its a Number:"
print("{} is {}".format(dig,res))