#test2 max function, average student function 

def main():
	#function make_list
	row = int(input("number of students "))
	col = int(input("number of courses "))
	grades = make_list(row, col)
	print(grades)	
	#to print in matrix form 
	for i in range(row):
		print(grades[i])
	
	#function max_value
	maxV, i_max, j_max = max_value(grades, row, col)
	print("maximum is ",maxV,"at row", i_max, "at column", j_max)
	
	ave_list = ave_student(grades, row, col)
	print(ave_list)
def max_value(grades, row, col):
	maxV = grades[0][0]
	i_max = 0 
	j_max = 0 
	 
	for i in range(row):
		for j in range(col):
			if(maxV<grades[i][j]):
				maxV = grades[i][j]
				i_max = i
				j_max = j
	return maxV, i_max, j_max			


def make_list(row, col):
	grades = [[0 for i in range(col)]for j in range(row)]
	for i in range(row):
		for j in range(col):
			grades[i][j]=int(input("enter grade "))
	
	return grades

def ave_student(grades, row, col):
	ave_list = []
	
	for i in range(row):
		sum = 0	
		for j in range(col):
			sum = sum+grades[i][j]
		ave = sum/col
		ave_list.append(ave)

	return ave_list

main()
