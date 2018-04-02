#Tyler Scott
#lab 6 
#problem 1

#Write a program that randomly generates the 2-dimensional list. Make 
#sizes of the list user input. Program prints the list in 3 different 
#ways: all elements on different rows, each row on separate line, and 
#list form ([[ first row], [second row]...[..]]

import random 


def make_list(scores, sizeRow, sizeCol):
	for i in range(sizeRow):
		for j in range(sizeCol):
			scores[i][j]=random.randint(0,9)
	return scores

def printmatrix(scores, sizeRow, sizeCol):
	for i in range(sizeRow):
		print(scores[i])
def matrix2(my_list):
	for i in range(row):
		for j in range(col):
			print(my_list[i][j])

def main():
	sizeR=int(input("enter the row size: "))
	sizeC=int(input("enter the column size: "))
	mlist=[[0 for i in range(sizeC)]for j in range(sizeR)]
	mlist=make_list(mlist, sizeR, sizeC)
	printmatrix(mlist, sizeR, sizeC)
	print(mlist)
		
main()
