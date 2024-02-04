#Program for finding common words among multiple lines.
#CommonWords.py
line1=input("Enter First  Line of text:")
line2=input("Enter Second  Line of text:")
print("-"*50)
print("Line1:{}".format(line1))
print("Line2:{}".format(line2))
print("-"*50)
lst1=line1.split()
lst2=line2.split()
st1=set(lst1)
st2=set(lst2)
cw=st1&st2
print("Number Common words={}".format(len(cw)))
print("List of Common words={}".format(cw))