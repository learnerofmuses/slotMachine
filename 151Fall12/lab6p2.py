#name:Tyler
#date:OCT22,2012

#write a program that calculates the insurance points that 3 different 
#people will receive for speeding on highway.
#The upper speed limit on highway is 65 mph.Assume that speed is integer 
#number.

def insurance(speed):
	if(speed>=90):
		print("You will receive 4 points")
	elif(speed>=80):
		print("You will receive 3 points")
	elif(speed>=70):
		print("You will receive 2 points")
	elif(speed>=66):
		print("You will receive 1 point")
	else:
		print("You will not obtain any points")

def main():
	speed1=int(input("enter speed for driver 1 "))
	speed2=int(input("enter speed for driver 2 "))
	speed3=int(input("enter speed for driver 3 "))
	print("number of points driver 1 will receive is")
	insurance(speed1)
	print("number of points driver 2 will receive is")
	insurance(speed2)
	print("number of points driver 3 will receive is")
	insurance(speed3)
main()

#Lab Report
#1. functions for this program are insurance and main
#2. main no parameters
#3. insurance - formal - speed
#actual speed1, speed2, speed3
#Inputs: driver1-89 driver2-55 driver3-76
#Outputs: driver1- 3 points, driver2- no points, driver3- 2 points

