ROW = 5 
COL = 4

def main():
	scores = [[0,0,0,0], [1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
	print(scores)

	for i in range(ROW):
		for j in range(COL):
			scores[i][j] = i+j

	print("after assigning values")
	print(scores)

	print("printing something - explain here what in printing")

	for i in range(ROW):
		if(i%2 == 0):
			print(scores[i])

main()













































