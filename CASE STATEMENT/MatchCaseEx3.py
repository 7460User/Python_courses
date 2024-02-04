#Program for demonstarting multiple case labels in match case stmt
#MatchCaseEx4.py
wkn=input("Enter the Week Name:")
match(wkn.upper()):
	case "MONDAY" | "TUESDAY" | "WEDNESDAY" | "THURSDAY" | "FRIDAY"):
		print("{} is Working Day:".format(wkn))
	case "SATURDAY":
		print("{} is WEEK END:".format(wkn))
	case "SUNDAY":
		print("{} is HOLI Day:".format(wkn))
	case _:
		print("{} is not a week day:".format(wkn))