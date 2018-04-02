#Write a function that accepts two parameters, integer and its size(the 
#number of the digits),and finds and prints the average of its EVEN digits.
#If there are no even digits in the parameter,
#the function prints an appropriate message. 
#Write a main function to test your function 

#example:
#2341890104 this is 10 digit number
#even digits are:2 4 8 0 0 4 - we have 6 even digits
#sum = 2+4+8+4= 18
#average = 18/6.0 = 3.0

def evenDigits(num, size):
	countEven = 0 
	sumEven = 0 

	for i in range(size):
		digit = num%10
		if(digit%2 == 0):
			sumEven = sumEven + digit
			countEven = countEven + 1
		num = num/10
	
	if(countEven > 0):
		ave = float(sumEven)/countEven
		print("the average is", ave)
	else:
		print("no even digits")


def main():
	num = int(input("enter positive number "))
	size = int(input("enter number of digits of the first input "))

	if((num>0) and (size>0)):
		evenDigits(num, size)
	else:
		print("invalid input")

main()
