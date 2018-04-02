def guess(my_list):
	m = len(my_list[0])
	index = 0
	for k in range(1, len(my_list)):
		length = len(my_list[k])
		if(m > length):
			m = length
			index = k
	return m, index

def main():
	my_list = ['yana', 'guy', 'python', 'course', 'land']
	m, index = guess(my_list)
	print(m, index, my_list[index])

main()
