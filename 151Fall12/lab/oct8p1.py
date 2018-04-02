
#write a function FtoC thats converts Fahrenheit temperature to Celsius
#write a second function CtoF that converts Celsius temperature to 
#Fahrenheit temperature
#This program will ask user to enter Fahrenheit for two days and find
#Celsius temperature for these two days.
#This program will also ask the user to enter Celsius for two days
#and find Fahrenheit temperature for these two days.

def FtoC(Fahrenheit):
	Celsius= float(5)/9*(Fahrenheit - 32)
	print(Celsius)

def CtoF(Celsius):
	Fahrenheit= float(9*Celsius/5) +32
	print(Fahrenheit) 

def main():
	Fahrenheit1= float(input("enter Fahrenheit temprature for day1 "))
	Fahrenheit2= float(input("enter Fahrenheit temperature for day 2 "))
	Celsius1= float(input("enter Celsius temperature for day 1 "))
	Celsius2= float(input("enter Celsius temperature for day 2 "))

	#Results:
	print("the temperature in Celsius when converted from Fahrenheit on day 1 is")
	FtoC(Fahrenheit1)
	print("the temperature in Celsius when converted from Fahrenheit on day 2 is")
	FtoC(Fahrenheit2)
	print("the temperature in Fahrenheit when converted from Celsius on day 1 is")
	CtoF(Celsius1)
	print("the temperature in Fahrenheit when converted from Celsius on day 2 is")
	CtoF(Celsius2)

main()

#1.Name of ALL functions in your program
#FtoC(Fahrenheit),CtoF(Celsius),main
#2.Name of formal and actual parameters for each function 
#Fahrenheit, Celsius
#4 functions called Fahrenheit1,Fahrenheit2,Celsius1,Celsius2
#input: (Fahrenheit1 87.5, Fahrenheit2 92.3, Celsius1 67.2, Celsius2 57.8)
#output:(Celsius 30.8, Celsius 33.5, Fahrenheit 152.96, Fahrenheit 136.04)

