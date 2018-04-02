#In the Gregorian calendar a year is a leap year when the number 
#representing it is divisible by 4, unless it is divisible by 100, unless 
#it is divisible by 400. Thus years such as 1996, 1992, 1988 and so on are 
#leap years because they are divisible by 4 but not by 100. For century 
#years, the 400 rule is important. Thus, century years 1900, 1800 and 1700 
#while all still divisible by 4 are also exactly divisible by 100. As they 
#are not further divisible by 400, they are not leap years. Also, you can 
#assume that there were no leap years before 1582. Write a program 
#LeapYear.py that asks the user to enter 7 different years and for each 
#year, computes whether that year is a leap year. YOU MUST USE LOOP FOR IN 
#YOUR PROGRAM

def leap(year):
	if(year>=1582):
		if(year % 4 == 0):
			if(year % 100 == 0):
				if(year % 400 == 0):
					print("yes")
				else:
					print("no")
			else:
				print("yes")
		else:
			print("no")
	else:
		print("not a leap year")
def main():
	for i in range(7):
		year = int(input("enter year "))
		if(year > 0):
			leap(year)
		else:
			print("not a leap year")

main() 
 
