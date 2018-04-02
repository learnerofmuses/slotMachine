#a. Write a function countValue that accepts FOUR parameters: 
#two-dimensional list of integers,  row and col (sizes of the list) 
#and the additional integer. The function returns 
#the amount of times that integer appears in the list. 

#b. Write a program  that inputs sizes of 2d list,  
#randomly generates TWO two-dimensional lists 
#of integers between 0 and 5, and generates additional integer between 1 
#and 5 to search for. The program finds the number of times 
#that integer appears in each 2d list.

#The program is partially written for you. Complete the program

import random

def countValue(my_list, row, col, num):
	counter = 0
	for i in range(row):
		for j in range(col):
			if(my_list[i][j]==num):
				counter+=1
	return counter		
def make_list(scores, row, col):
        for i in range(row):
                for j in range(col):

                        scores[i][j]=random.randint(0,5)
        return scores

def printMatrix(scores, row, col):
        for i in range(row):
                print(scores[i])

def main():
	row=int(input("enter row size: "))
	col=int(input("enter column size: "))
	findnum=int(input("enter number to count: "))
	scores=[[0 for i in range(col)]for j in range(row)]
	scores2=[[0 for i in range(col)]for j in range(row)]
	make_list(scores, row, col)
	make_list(scores2, row, col)
	count=countValue(scores, row, col, findnum)
	count2=countValue(scores2, row, col, findnum)
	printMatrix(scores, row, col) 
	print()

	print("here is list1: ")
	if(count==0):
		print("no", findnum, "in this list")
	else:
		print("there are", count, "in this list")
	
	printMatrix(scores, row, col)
	print()
	
	print("here is list2: ")
	if(count==0):
		print("no", findnum, "in this list")
	else:
		print("there are", count2, "in this list") 
	
main()
