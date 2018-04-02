#what is the output of the following program
#write your answer BEFORE you run the program
#then RUN the program and compare

#GRADE YOURSELF!
ROW = 5
COL = 4

def main():
	scores=[[0,0, 0, 0], [1, 1, 1, 1], [2,2, 2, 2], [3,3, 3, 3], [4, 4, 4, 4]]
	print(scores)
	
	
	for i in range(ROW):
		for j in range(COL):
			scores[i][j] = i+j

	print("after assigning values")
	print(scores)	

	print("Printing something - explain here what is printing ")

	for i in range(ROW):
		if(i%2 == 0):
			print(scores[i])
main()

