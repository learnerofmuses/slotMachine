#Write a program that reads one positive integer and finds the sum and the 
#average of the digits.

#example: input 3456 output sum = 3+4+5+6 = 18, ave = 18/4.0 = 4.5
#input 78 output sum = 15 ave 15/2/0 = 7.5

def digits(number):
	countDigit = 0 
	totalDigit = 0 
	
	while(number > 0):
		totalDigit = totalDigit + number % 10
		countDigit = countDigit + 1
		number = number/10

	aveDigit = float(totalDigit)/countDigit
	print("the sum of digits is ", totalDigit)
	print("the average of digit is", aveDigit)

def main():
	num = int(input("enter integer "))
	if(num > 0):
		digits(num)
	else:
		print("your input is invalid ")
main()

#lab report
#input 0 input output - invalid input
#input -2 output - invalid input
#input 437428 output sum = 28, average = 4.666667
#output is correct since the program performs:
#totalDigit = 4+3+7+4+2+8 = 28
#countDigit = 6
#aveD