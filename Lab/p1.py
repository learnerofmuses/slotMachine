#name: Tyler
#date: OCT 1 2012

#Write a Python program that promts the user to enter one 
#number that indicates the radius of the circle.
#The program will calculate and print the diameter 
#(2*radius),circumference (2*pi*radius) and area 
#(pi*radius*radius) of the circle. Use the value 3.14159 for 
#PI.Write separate function for each task. Main function will 
#be responsible for reading the input value and using 
#functions you write to calculate diameter, circumference 
#and area of the circle.
 
#Input 

PI = 3.14159
 
def diameter(radius):
	diameter = 2 * radius 
	print(diameter)

def circumference(radius):
	circumference = 2 * PI * radius 
	print(circumference)

def area(radius):
	area = PI*radius*radius 
	print(area)
#Results:

def main():
	radius = float(input("please enter radius number "))
	

	print("the diameter is")
	diameter(radius)
	print("the circumference is")
	circumference(radius)
	print("the area is")
	area(radius)

#Call the main function 

main() 
