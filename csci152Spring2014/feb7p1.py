#write a program that first randomly generates the list
#of integers between -1 and 1, and then removes all zero 
#values from the list 

import random

def main():
	size = int(input("enter the size of the list "))
	list_result = make_list(size)
	print("randomly generated list ")
	print(list_result)

	remove_all(list_result, 0)
	print("list after removal is ")
	print(list_result)
def make_list(size):
	my_list = []
	for i in range(size):
		my_list.append(random.randint(-1, 1))
	return my_list


def remove_all(my_list, item):
	while(item in my_list):
		my_list.remove(item)
	
main()
