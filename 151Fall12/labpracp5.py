#Tyler
#Nov 26 2012
#Write a program that geneates 100 random numbers, and keeps a count
#of how many of those random numbers are even and how many are odd.

import random 

def divTwo(num):
	if(num%2 == 0):
		result = True
	else:
		result = False
	return result
def main():
	countOdd = 0
	countEven = 0
	for i in range(100):
		num = random.randint
	
		if(divTwo(num)):
			countEven = countEven + 1
		else:
			countOdd = countOdd + 1
main()
			
