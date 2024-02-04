
#CountChars.py
line=input("Enter Line of Text:")
d={} # Empty dict
for ch in line:
	if ch in d:
		d[ch]=d[ch]+1
	else:
		d[ch]=1
else:
	print("Given Line:{}".format(line))
	for c,nc in d.items():
		print("\t{}->{}".format(c,nc))
	