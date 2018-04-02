#Write a function that finds and returns the number of even and number of odd elements in 2-dimensional list, their sums and averages. Write main to test your program. Pay attention, 
#if there are no even elements or no odd element, the first return value will be 0, the sum and average could be any numbers and you would need to use if statemet to print correct 
#results. 

import random

def main():
	row = int(input("enter the number of rows: "))
	col = int(input("enter the number of columns: "))
	even = [] 
	odd = [] 
	cE = 0
	cO = 0
	a = [[ 0 for i in range(col)] for j in range(row)] 	

	for i in range(row):
		for j in range(col):
			a[i][j] = random.randint(0, 20)
	print a

	for i in range(row):
		for j in range(col):
			if(a[i][j]%2 !=0):
				print(a[i][j])
				odd.append(a[i][j])
				sum = cO+1
			average = sum/a[i][j] 
			elif(a[i][j]%3 !=0):
				print(a[i][j])
				even.append(a[i][j])
				sum = cE+1
			average = sum/a[i][j]
	
	return 0, sum, average
	
def make_list():	
	if(len(odd)==0):
		print("no odd numbers")
	else:
		print("odd numbers")
	
	print(odd)

	if(len(even)==0):
		print("no even numbers")
	else:
		print("even numbers")
	
	print(even)


main()
