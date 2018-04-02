#Tyler
#Jan 16 2013

import math 

def quadratic(a, b, c):
	d = b ** 2 - (4 * a * c)
	if (d > 0):
		x1 = (-b + math.sqrt(d))/(2*a) 
		x2 = (-b - math.sqrt(d))/(2*a)
		return True, x1, x2
	elif (d == 0):
		x1 = float(-b)/(2*a)
		return True, x1, x1
	else: 
 		return False, 0, 0
