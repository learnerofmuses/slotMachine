def guess(my_list, sizeR, sizeC):
	count = 0 
	newi = []
	newj = []
	for i in range(sizeR):
		for j in range(sizeC):
			if(my_list[i][j]%5!=0):
				count = count + 1
				newi.append(i)
				newj.append(j)
		return count, newi, newj
	
def main():
	my_list = [[3, 5, 10, 15], [1, 7, 5, 25], [7, 5, 12, 35]]
	count, newi, newj = guess(my_list, 3, 4)
	print(count)
	for k in range(len(newi)):
		print(newi[k], newj[k])

main()
