#Program for demonstarting multiple case labels in match case stmt
#MatchCaseEx5.py
wkn=input("Enter the Week Name:")
match(wkn[0:3].upper()):
	case "MON" | "TUE" | "WED" | "THU" | "FRI":
		print("{} is Working Day:".format(wkn))
	case "SATURDAY":
		print("{} is WEEK END:".format(wkn))
	case "SUNDAY":
		print("{} is HOLI Day:".format(wkn))
	case _:
		print("{} is not a week day:".format(wkn))