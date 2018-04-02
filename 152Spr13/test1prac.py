def word_index(my_list, word):
	index_new = []
	for i in range(len(my_list)):
		if(my_list[i] == word):
			index_new.append(i)
	return index_new

def main():
	print("part III")
	my_list =[3, 9, 10, 12, 1, 7, 5, 27, 14, 18]
	index_new=something(my_list)


main()
