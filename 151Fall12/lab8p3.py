#name:Tyler
#date:Nov 12 2012
#Write a program that prompt the user to enter 10 integers. The program 
#will determine and print the maximum and minimum among the input numbers. 
#YOU MUST USE LOOP FOR IN YOUR PROGRAM

def minMax(size):
	num = int(input("enter first number "))
	max = num 
	min = num 
	for i in range(size - 1):
 		num = int(input("enter next int "))
		if(num > max):
			max = num
		if(num < min):
			min = num
			print("max is")
			print(max)
			print("min is")
			print(min)
def main():
	size = int(input("enter your input "))
	minMax(size)
main()


