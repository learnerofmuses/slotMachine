#Tyler Scott
#FEB 12 2013 

#Write a program that randomly generates the 2-dimensional list. Make 
#sizes of the list user input. Program prints the list in 3 different ways: 
#all elements on different rows, each row on separate line, and list form 
#([[ first row], [second row]...[..]]

import random 
ROW = 4
COL = 4


def list(sizeRow, sizeCol, scores):

	for i in range(sizeRow):
		for j in range(sizeCol):
			

def main():
	
	scores = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
	print (scores)
	
	for i in range(ROW):
		for j in range(COL):
			scores[i][j] = random.randint(1,7)

	print("after assigning random values")
	print(scores)
	print("matrix form")
	for i in range(ROW):
		print(scores[i])
		
	
	
	print("all elements in one column")
	for i in range(ROW):
		for j in range(COL):

			print(scores[i][j])
	
main()
