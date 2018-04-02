def guess(my_list):
	count = 0 
	sum = 0 
	new_list = []

	for i in my_list:
		if(i%3 == 0):
			count = count + 1
			sum = sum + i 
			new.append(i)

	if(count == 0):
		average = -1 
		sum = -1 
	else:
		average = float(sum)/count
	
	return count, sum, average 

def something(my_list):
	index_new = []
	
	for i in range(len(my_list)):
		if(my_list[i] % 2 != 0):
			index_new.append(i)
	return index_new

