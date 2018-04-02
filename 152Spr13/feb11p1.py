#this program shows how to work with 2-dimensional lists 

import random 
RPW = 3
COL = 4

def sumave(scores, sizeRow, sizeCol):
	#this function returns sum and average 
	#of all elements in 2 dimensional lists

	sum = 0 
	for i in range(sizeRow):
		for j in range(sizeCol):
			sum = sum + scores[i][j]
	average = float(sum)/(sizeRow*sizeCol)
	return sum, average 

def main():
	#definition of the 2-dim list 
	
	scores = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
	print(scores)

	#assigning random values to 2-dim list 
	for i in range(ROW):
		for j in range(COL):
			scores[i][j] = random.randint(1,5)

	print("after assigning random values")
	print(scores)
	print("how to print a matrix")
	for i in range(ROW):
		print(scores[i])
	
	print("all elements in in one column")
	for i in range(ROW):
        	for j in range(COL):

			print(scores[i][j]) 	
	
	print("sum and average of all elements")
	sum, average=sumave(scores, ROW, COL)
	print(sum, average)	

main()
