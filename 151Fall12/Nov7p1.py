#this program demonstrates how to work with loop for 

#there are 2 types of loops: counter-control repetition and
#sentinel controlled repetition

#in counter-controlled repetition it is known upfront
#the number of iterations your loop will perform 
#example: your program reads 5 integers and finds their sum .

#in sentinel-controlled repetition you have a condition that 
#terminates the loop, and the number of iterations unknown and
#different in defference executions
#example: you write a program that reads a sequence of positive integers 
#and first negative terminates the input
#another example the sum/average digit program that we did on nov 5
#in this program loop executes until number is positive.

#loop for is used only for counter-controlled repetitions

def main():
	print("first loop")
	for num in range(5):
		print(num)

	#this loop will print
	#0
	#1
	#2
	#3
	#4
	#in general range(k) will run from 0 to k-1
	print("second loop")
	for i in range(3):
		print(i+1)

	#the ouput:
	#range(3) will run from i=0 to i=2
	#print(i+1) will print numbers from 1 to 3
	#you can determine start and end in range 
	#range (start, end) it will run from start to end-1
	
	print("third loop")
	for num in range(5,8):
		print(num)

	#the output is:
	#5
	#6
	#7

	#you can also determine the step 
	#range(start, end, step) it will print from start 
	#in step jumps until end-1

	print("fourth loop")
	for num in range(1, 10, 3):
		print(num)
	#output:
	#1
	#4
	#7

	print("fifth loop")
	for name in ['Yana', 'Guy', 'Bony']:
		print(name)

	#did not use function range because function range is for numbers 
	#only 


	print("sixth loop")
	counter = 0 
	for letter in ['A', 'B', 'B', 'C', 'Z', 'B']:
		if(letter == 'B'):
			counter = counter + 1
		
	print(counter)
	
	#the output is 3
	#this program counts the amountof B's in the list

main()

