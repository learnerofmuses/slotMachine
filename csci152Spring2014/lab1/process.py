#in this file we will write 5 functions:
#countCapital, countLow, countDigit, countRest, percent

import random

def countCapital(size):
	count = 0 
 	for i in range(size):
		num = random.randint(32, 126) 
		ch = (chr)(num)
		print(num, ch)
		if(ch>= 'A' and ch<= 'Z'):
			counter +=1
	return counter

#def countLow(size):
#def countDigit(size):
#??def countRest(size):

def percent(counter, size):
	return 100*((float)(counter)/size)
