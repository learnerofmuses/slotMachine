def guess(my_list):
	count = 0 
	sum = 0 
	new = []

	for i in my_list:
		
		if(i % 3 == 0):
			count = count+1 
			sum = sum + i 
			new.append(i)
	if(i % 2 == 0):
		print("invalid input")
	else:
		average = float(sum)/count

	return sum, average, new 

def main():
	my_list = [3, 6, 5, 7, 2, 45, 12, 9, 24, 27, 33]
	sum, average, new = guess(my_list)
	print(sum, average, new)

main()
