#write a program that randomly generates characters and finds
#how many characters of some kind do you have and its percentage 

#example: 

#we generate 10 characters 
#a * 9 ) 0 P U j % ^ 
#and say we would like to count how many capital letters 
#and percentage:
#2 capital letters 
#percentage: (2/10)*100

import process
import random
def main():
	menu(1)
def menu(choice):

	if (choice == 1):
		size = random.randint(5,15)
		print("size is ", size)
	cP = process.countCapital(size)
		if(cP ==0):
			print("no capitals in your pool")
		else:
			capitalPercent = process.percent(cP, size)
			print("there are ", cP, "capitals")
			print("their percent is ", capitalPercent)

	else:
		size = random.randint(5,15)
		print("size is", size)
		capital = process.countCapital(size)
		low = process.countLow(size)
		digit = process.countDigit(size)

		rest = size - (capital+low+digit)
		if(rest==0):
			print("we dont have anything else")
		else:
			restPercent = process.percent(rest,size)
			print("there are ", rest," other chars")
			print("their percent is ", restPercent)			
main()
