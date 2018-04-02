#Rolling dice game is rolling the dice several times. The number of times 
#the dice is rolled is function parameter. The function finds and returns 
#the number of times each number 1, 2, 3, 4, 5, or 6 is appeared.

#Store the function that simulates rolling dice game in separate file, 
#dice.py. To play the game, for each loop iteration, program randomly 
#generates the integer between 1 and 6 and update the appropriate 
#count

import random
min = 1
max = 6

def dice_roll():
	count = 0
	
	play = input("would you like to roll the dice?: ")
	roll = "yes"
	
	while(roll == "yes"):
		print random.randint(min, max)
		count +=1
		play = input("roll again?: ")

	return min, max, count		
