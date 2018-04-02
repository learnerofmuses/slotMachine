#2-D lists
#write a function that counts the number of zeros in 
#2d list
#write a function corner, that checks if
#the element is a corner element in the 2D list 
import random
MAX=1
MIN=0

def corner(list2d, row, col, i, j):
	if(i==0 and j==0):
		return True
	elif(i==0 and j==col-1):
		return True
	elif(i==row-1 and j==0):
		return True
	elif(i==row-1 and j==col-1):
		return True
	else:
		return False 

def count_value(list2d, row, col, value):
	counter = 0 
	for i in range(row):
		for j in range(col):
			if(list2d[i][j]==value):
				counter+=1
	return counter
	
def print_table(list2d, row, col):
	for i in range(row):
		print(list2d[i])
def make_2d_list(list2d, row, col, min, max):
	#this will require 2d list declaration in main
	
	for i in range(row):
		for j in range(col):
			list2d[i][j]=random.randint(min,max)


def main():
	row = int(input("enter row size: "))
	col = int(input("enter col size: "))
	a = [[ 0 for i in range(col)] for j in range(row)]
	make_2d_list(a, row, col, MIN, MAX)
	print_table(a, row, col)
	print("the number of ", 0)
	print(count_value(a, row, col, 0))
	#value = int(input("enter value to count "))
	#print(
main()
