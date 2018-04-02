#name: Tyler
#date: OCT 8
#Write a function that finds and prints an average of the digits 4-digit positive integer
#Write a function that finds and prints an average of three integer numbers
#Write a function that finds and prints an average of the last digits of three
#integer numbers
#Write a program that first reads 3 integers and finds their average of their last digits.
#The program asks the user to enter one 4-digit integer number and find average of input number

def aveDigits(num):
	digitLast= num % 10  
	num= num / 10 
	digitMid = num % 10 
	num= num / 10 
	digitMiD = num % 10
	num = num / 10
	digitFirst= num % 10 
	num= num / 10
	
	sum= digitLast + digitMid + digitMiD + digitFirst
	aveDigits= float(sum)/4 
	print(aveDigits)

def average(d1, d2, d3):
	average= float(d1 + d2 + d3)/3
	print(average)

def aveLast(num1, num2, num3):
	dl1= num1 % 10
	dl2= num2 % 10
	dl3= num3 % 10
	
	sum= ld1 + ld2 + ld3
	aveLast= float(sum)/3
	print(aveLast)
def main():
	#Input:

	num= int(input("enter 4-digit positive integer "))
	d1= int(input("enter first digit number "))
	d2= int(input("enter second digit number "))
	d3= int(input("enter third digit number ")) 

	#Results:
	
	print("the average of the 4-digit positive integer is ")
	aveDigits(num)
	print("the average of the three integer numbers is ") 
	average(d1, d2, d3)
	print("the average of the last digits of three integer numbers is ")
	aveLast(num1, num2, num3)

main()
	

