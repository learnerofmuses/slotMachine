#Tyler
#Nov 26 2012
#write a function named falling_distance that accepts an object's falling 
#time in seconds as an argument. The function should return the distance 
#in meters that the object has fallen during that time interval. Write
#a program that calls the function in a loop that passes the values
#1 through 10 as arguments and displays the return value. 

g = 9.8
def falling_distance(time):
	distance = (1/2.0)*g*time**2
	return distance

def main():

	for i in range(1, 11):
		result = falling_distance(i)
		print(result)
		
main() 

