def deadpool(my_list):
	pos = 0
	neg = 0 
	zero = 0 
	
	for i in my_list:
		if(i > 0):
			pos = pos + 1
		elif(i < 0):
			neg = neg + 1
		else:
			zero = zero + 1
	return pos, neg, zero

def main():
	my_list = [1, -5, 3, 7, -11, 39, 0, -15, -23]
	pos, neg, zero = deadpool(my_list)
	print(my_list)
	print("there are", pos, "positive numbers")
	print("there are", neg, "negative numbers")
	print("there are", zero, "zero numbers")
main()
