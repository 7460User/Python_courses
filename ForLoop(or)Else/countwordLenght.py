#Program for finding even length words from given line of text
#CountOddlengthWords.py
line=input("Enter a Line of text:")
print("\nGiven Line of Text:{}".format(line))
words=line.split()
for word in words:
	if (len(word)%2!=0):
		print("\t{}".format(word))
	