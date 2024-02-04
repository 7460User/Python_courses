wkn=input("Enter Weekname:")
match(wkn.upper()):
	
	case "MONDAY":
		print("\t{} is Working Day:".format(wkn))
	case "TUESDAY":
		print("\t{} is Working Days:".format(wkn))
	case "WENESADAY":
		print("\t{} is totak Workind days:".format(wkn))
	case "THRSDAY":
		print("\t{} is Working Day:".format(wkn))
	case "FRIDAY":
		print("\t{} is Working Days:".format(wkn))
	case "SATRADAY":
		print("\t{} is totak Workind days:".format(wkn))
	case "SUNDAY":
		print("\n{} is totak Workind days:".format(wkn))
	case _:
		print("\t{} is not a week day:".format(wkn))
	


	
	
