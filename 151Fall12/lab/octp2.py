#name: Tyler
#date: OCT 8 2012
#Write a function FtoC that converts Fahrenheit temperature to Celsius
#Write a second function CtoF that converts Celsius temperature to Fahrenheit
#This program will ask the user to enter Fahrenheit temperature for two days
#and find corresponding Celsius temperature for these two days.
#This program will aso ask user to enter Celsius temperature for two days
#and find corresponding Fahrenheit temperature for two days.

#Part I:

def FtoC(Celsius):
	Celsius=(5/9)*(Fahrenheit - 32)
	print(Celsius)

def CtoF(Fahrenheit):
	Fahrenheit=(9*Celsius/5)+32
	print(Fahrenheit)

def main():
	#Input
	Fahrenheit1= float(input("enter Fahrenheit temperature for day 1 "))
	Fahrenheit2= float(input("enter Fahrenheit temperature for day 2 "))
	Celsius1= float(input("enter Celsius temperature for day 1 "))
	Celsius2= float(input("enter Celsius temperature for day 2 "))

	#Results:
	
	print("the temperature in Celsius when converted from Fahrenheit on day 1 is")
	FtoC(Celsius1)
	print("the temperature in Celsius when converted from Fahrenheit on day 2 is")
	FtoC(Celsius2)
	print("the temperature in Fahrenheit when converted from Celsius on day 1 is")
	CtoF(Fahrenheit1)
	print("the temperature in Fahrenheit when converted from Celsius on day 2 is")
	CtoF(Fahrenheit2)
main()
