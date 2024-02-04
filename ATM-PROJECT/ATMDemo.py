import sys
from ATMMenu import menu
from ATMExcept import DepositError,InsuffFundError,WithdrawError
from ATMoperactions import deposit,withdraw,balenq
while(True):
	try:
		menu()
		ch=int(input("Enter ur Choice:"))
		match(ch):
			case 1: 
				try:
					deposit()
				except ValueError:
					print("Don't try to deposit alnums, strs and symbols-Invalid Trans")
				except DepositError:
					print("Don't enter -Ve / Zero for Deposits:")
			case 2: 
				try:
					withdraw()
				except ValueError:
					print("Don't try to withdraw alnums, strs and symbols-Invalid Trans")
				except WithdrawError:
					print("Don't enter -Ve / Zero for Withdraws :")
				except InsuffFundError:
					print("Ur Account have Insufficient Funds--Read Python Notes:")
			case 3:
				balenq()
			case 4: 
				print("Thx for using program")
				sys.exit()
			case _: 
				print("Ur Selection of Operation is wrong and try again")
	except ValueError:
		print("Don't enter strs, alnums and symbols for Choice:")

