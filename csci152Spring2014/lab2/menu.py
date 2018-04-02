#Write a menu function that will allow user to choose an appropriate 
#game. You can assume that choice 1 indicates dice game and choice 2 
#indicates coin game.
#Import both files and use the appropriate function based on the menu 
#choice.

import dice
import coin
 
def main():
	print("enter your choice: 1 for dice and 2 for coin ")
	choice = int(input(" "))
	if(choice == 1):
		min, max, count = dice.dice_roll()		





	elif(choice == 2):
		count1, count2 = coin.cointossing()		
main():		
