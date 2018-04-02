#working with 2-D lists

#program finds sum and average of elements in 2-d list
#program finds the number of elements equal to 
#specified value


import random
def main():
	row = random.randint(3,5)
	col = random.randint(3, 5)
	my_list = [[ 0 for i in range(col)] for j in range(row)] 
	print(my_list)
	for i in range(row):
		for j in range(col):
			my_list[i][j]=random.randint(-5,5)
		print("\nmy list \n")
	for i in range(row):
		print(my_list[i])
		
	sum = 0
	for i in range(row):
		for j in range(col):
			sum = sum + my_list[i][j]
	print("\n the sum of all elements is  ", sum)
	print("\n average is ", sum/(row*col))

	value = int(input("enter value to count "))
	result = search(my_list, row, col, value)
	if(result==0):
		print(value, "not in the list ")
	else:
		print(value, "appears", result, "times")
def search(my_list, row, col, value):
#always will send lists and sizes (row, col)
	count = 0
	for i in range(row):
		for j in range(col):
			if(value==my_list[i][j]):
				count+=1
	return count

main()

