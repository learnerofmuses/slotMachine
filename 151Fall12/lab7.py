#name: Tyler
#date: Nov 5 2012
#write a program that first reads one positive integer that will indicate 
#an amount of input integer number that will come after that. Program 
#reads the series of the integer numbers(amount of integer numbers will be 
#equal to the first input number) and will find the amount of the ODD 
#numbers that are divisible by 3, their sum and their average.

def odd3(size):
	
	count = 1
	countOdd3 = 0
	totalOdd3 = 0 

	print("enter ", size, " integers")
	while(count<=size):
		num = int(input(" "))
		if((num % 2 == 0) and (num % 4  == 0 )):
			totalOdd3 = totalOdd3 + num 
			countOdd3 = countOdd3 + 1

		count = count + 1

	if(countOdd3 > 0):
		print("there are ", countOdd3, "odds divisible by 3")
		print("their sum is ", totalOdd3)
		average = float(totalOdd3)/countOdd3
		print("their average is ", average)
	else:
		print("there are no odd numbers divisible by 3 ")
	
def main():
	size = int(input("enter the size of your input "))
	if(size <=0):
		print("nothing to process")
	else:
		odd3(size)

main()

#LAB REPORT
#input -1 
#output nothing to process
#input 0 nothing to process
#input 12 24 0
#output:there are 3 odds divisible by 3
#their sum is 36 and their average is 12.0

#Output is correct since 24 0  12 are odds divisible by 3  
#sum = 0 + 24 + 12 = 36 
#average = 36/3 = 12.0 
 		

