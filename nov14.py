#write function that has one parmeter -positive integer number, the 
#funtion finds the average of the even divisors only. The function
#also prints the amount of eve divisors and their sum.

#write a program that reads a sequence of positive integers, 
#first zero or negative will terminate the loop and for each 
#inout use the function you wrote to find sum, average and amount of 
#even divisors

def evenDivisor(num):
	countEven = 0 
	sumEven = 0 
	
	for i in range(1, num+1):
		if(num % i == 0 and i % 2 == 0):
			countEven = countEven + 1
			sumEven = sumEven + i
	if(countEven > 0):
		ave = float(sumEven)/countEven
		print("there are ", countEven, "even divisors")
		print("their sum is ", sumEven)
		print("their average is ", ave)
	else:
		print(num, "doesn't have any even divisors")

def main():
	num = int(input("enter positive integer "))
	if(num>0):
		while(num>0):
			print("processing even divisors of", num)
			evenDivisor(num)
			num = int(input("enter positive int"))
		
	else:
		print("nothing to process")
main()

#what will be the following output of this program for the following 
input:
#12 8 15 -2

#solution:
#num = 12 and the funtion is called
#in the function even divisors are: 2, 4, 6, 12
#their sum is: 2+4+6+12 = 24
#their are 4 even divisors and the average is 24/4.0 = 6.0
