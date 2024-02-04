def pailandram(s):
    return s == s[::-1]
# Driv Code
s = "hhhhh"
ans =  pailandram(s)
if ans:
    print("yes")
else:
    print("no")