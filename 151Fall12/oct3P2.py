#name: Tyler
#date: OCT 3 2012
#solution to program 1 on p.114

#we write one function km_to_mile that has
#one parameter the amount of kilometers and prints the correspondent
#number of miles 
#use the formula 
#miles = km * 0.6214

#write a main that ask three people to enter distance in km
#and find the distance in miles

CONVERT = 0.6214

def km_to_mile(km): 
	
	print(CONVERT*km)

def main():
	distance1 = float(input("enter first distance "))
	distance2 = float(input("enter second distance "))
	distance3 = float(input("enter third distance "))

	#function calls:
	
	print("miles for distance 1 ")
	km_to_mile(distance1)
	print("miles for distance 2 ")
	km_to_mile(distance2)
	print("miles for distance 3 ")
	km_to_mile(distance3)

main()
