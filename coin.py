#Scott
#Jan 23

import random

def coin(toss):
	
	heads = 0 
	tails = 0
	
	for i in range(toss):
		x = random.randint(1,2)
		if(x == 1):
			heads = heads + 1
			print x	
		elif(x == 2):
			tails = tails + 1
			print x
	return heads, tails
#LAB REPORT
#Input		      / Processing		     / Output
#-----------------------------------------------------------------------
#the number of times  / reads the number of times    / returns the number of times heads
#coin is tossed       / tossed and counts the number / was flipped and the number of 
#		      / of heads and tails	     / times tails was flipped


