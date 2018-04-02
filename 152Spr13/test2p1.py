def guess(my_list, sizeR, sizeC):
	count = 0

	for i in range(sizeR):
		for j in range(sizeC):
			if(my_list[i][j]%3==0):
				count = count+1
				my_list[i][j]= -1
	return count, my_list

def main():
	my_list = [[3, 5, 10, 15], [1, 7, 5, 27], [7, 5, 12, 34]]
	count, new = guess(my_list, 3, 4)
	print(count)
	print(my_list)

main()

