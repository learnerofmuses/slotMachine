#Throwing coin game is the game that flips coin several times. The number 
#of times the coin is flipped is function parameter. Function finds the 
#number of times HEAD and TAIL appear. You can assume, that 1 represents 
#TAIL and 2 represents HEAD.
#Store the function that simulates the flipping coing game in separate 
#file, coin.py. To play the game, for each loop iteration, program 
#randomly generates the integer between 1 and 2 and update the 
#appropriate counter.

import random

def cointossing():
	count1 = 0 
	count2 = 0 
	
	for x in range(6):
		z = randint(1, 2)
		if(z == 1):
			print("you have flipped HEADS")
			count1 +=1
		else:
			print("you have flipped TAILS")
	return count1, count2

