#2d list example

import random
ROW = 5
COL = 4

def main():
	a = [[0 for i in range(COL)]for j in range(ROW)]
	print(a)
	print("print 2D list as a table")
	for i in range(ROW):
		print(a[i])
	
	print("after random assignment ")
	for i in range(ROW):
		for j in range(COL):
			a[i][j]=random.randint(-5,5)
	
	for i in range(ROW):
		print(a[j])	

main()
