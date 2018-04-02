#Write a program that reads one positive integer
#and prints all divisors of the input number, 
#finds and prints the sum of the ALL divisors of the 
#input number and their average. If the input is negative or zero, the 
#program prints an error message.
#We will have 2 functions - one using loop FOR and one using loop WHILE

#Input: 24
#output: divisors: 1, 2, 3, 4, 6, 8, 12, 24 
#sum = 60 
#ave = 60/8.0 = 7.5

def divisorFor(num):
	countDivisor = 0 
	sumDivisor = 0 
	print("divisors are ")
	for i in range(1, num + 1):
		if(num % i == 0):
			print(i)
			countDivisor = countDivisor + 1
			sumDivisor = sumDivisor + i
	ave = float(sumDivisor)/countDivisor
	print("there are", countDivisor, "divisors")
	print("their sum is", sumDivisor)
	print("their average is", ave)

def main():
	num = int(input("enter number "))
	if(num>0):
		divisorFor(num)
	else:
		print("invalid input")
main()
