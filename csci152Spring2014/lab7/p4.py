#Write a function that finds and returns the number of elements that are divisible by 3. Function also creates and returns the new ONE-DIMENSIONAL list that includes all elements 
#that are divisible by 3. Write main to test your program 

def main():

	row = int(input("enter the number rows: "))
	col = int(input("enter the number of columns: "))
	min = int(input("enter min value of ints: "))
	max = int(input("enter max value of ints: "))
	
	list1= make_list(row, col, min, max)
	a = [[ 0 for i in range(col)] for j in range(row)] 
	
