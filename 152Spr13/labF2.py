#Linear funtion 
	
import math 
def linear(b, c):
	 
	if(b != 0):
		x1 = float(-c)/b
		return True, x1
	elif (b == 0 and c != 0):
		return False, 0
	elif (b == 0 and c == 0):
		return False, 1 	
		
