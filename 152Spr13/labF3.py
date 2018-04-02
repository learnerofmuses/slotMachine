#this program solves quadratic and linear equations.

import labF1 
import labF2
 
def main():
	size = int(input("enter number of times to run "))
	for i in range(size):
		a = int(input("enter the value for a "))
		b = int(input("enter the value for b "))
		c = int(input("enter the value for c "))
		if(a == 0):
			res, x1 = labF2.linear(b,c)
	
			if(res == True):
				print "x1", x1	
			elif(res == False and x1 == 0):	 
				print "no solutions"
			elif(res == False and x1 == 1):
				print "infinite solutions"
		
		else: 
			res,x1,x2 = labF1.quadratic(a,b,c)
			if (res == True and x1 == x2):
				print "x1 =", x1
			elif (res == True):
				print "x1=", x1, "x2=", x2
			elif (res == False):
				print "no solutions"

main()
