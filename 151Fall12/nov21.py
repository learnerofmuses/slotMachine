#write a program that reads sequence of positive integers
#first zero or negative will terminate the input
#for each input, program finds the number of digits and their
#average
def main():
	num = int(input("enter positive int "))
	while(num>0):
		sumDigit = 0 
		numDigit = 0
		
		#the inner loop will process one input
		#and find number of digits and their sum

		print("processing ", num)

		while (num != 0):
			digit = num%10
			sumDigit = sumDigit + digit
			numDigit = numDigit + 1
			num = num/10
	
			#after the loop we can 
			#average of digits for one input

		average = float(sumDigit)/numDigit
		print("num of digits is", numDigit)
		print("average of digits is", average)
		#reading next input
		num=int(input("enter positive integer "))
main()
