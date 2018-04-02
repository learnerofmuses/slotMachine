#Write a function countValue that accepts FOUR parameters: 
#two-dimensional list of integers, sizeR and sizeC (sizes of the list) and 
#the additional integer. 
#The function returns the amount of times that integer appears in the list. 

#Write a function maxList that accepts FOUR parameters: 
#TWO two-dimensional lists of integers (assume that both lists has the same 
#size), and the sizes of the lists ? sizeR and sizeC. The function 
#randomly generates integer between 1 and 100. 
#The function counts the number of times this integer appears in each 
#list. Use function countValue to perform this task. The function returns 
#the list with the maximal amount of appearances. 

import random
ROW = 4
COL = 4
RANGE = 5

def countValue(my_list, sizeR, sizeC, num):
	count = 0 
	for i in range(sizeR):
		for j in range(sizeC):
			if(my_list[i][j] == num):
				count = count + 1
	return count 

def maxList(listA, listB, sizeR, sizeC):
	num = random.randint(1, range)
	print("number to look for is", num)
	countX = countValue(listA, sizeR, sizeC, num)
	countY = countValue(listB, sizeR, sizeC, num)
	if(countX > countY):
		return listA
	elif(countX < countY):
		return listB

def list(scores, sizeRow, sizeCol):
	for i in range(sizeRow):
		for j in range(sizeCol):
	
			scores[i][j] = random.randint(0, num)
	return scores

def printMatrix(scores, sizeRow, sizeCol):
	for i in range(sizeRow):
		print(scores[i])

def main():
	a = [[ 0 for i in range(COL)] for j in range(ROW)]
	b = [[ 0 for i in range(COL)] for j in range(ROW)]
	max_list = [[ 0 for i in range(COL)] for j in range(ROW)]
	a = list(a, ROW, COL, range)
	b = list(b, ROW, COL, range)
	print("first")
	printMatrix(a, ROW, COL)
	print("second")
	printMAtrix(b, ROW, COL)
	print("list with max amount is")
	max_list = maxList(a, b, ROW, COL)
	if(max_list != None):
		printMatrix(max_list, ROW, COL)
	else:
		print("lists have same number of value")

main()
