def guess(my_list, num):
	count = 0 
	new = []
	
	for i in my_list:
		if(i == num):
			count = count +1
			new.append(i)
	return count, new 

def main():
	my_list = [3, 5, 10, 15, 1, 7, 5, 27, 7, 5, 12, 34, 5]
	num_to_look = 5
	count, new = guess(my_list, num_to_look)
	if(count > 0):
		print(count, new)
	else:
		print(num_to_look, "not in the list")
main()	
