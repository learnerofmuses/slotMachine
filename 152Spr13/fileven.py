def sumCount(size):
	countEven = 0 
	sumEven = 0 
	print("enter ", size, "ints ")
	for i in range(size):
		n = int(input(""))
		if(n%2 == 0):
			countEven+=1
			sumEven+=n
		return countEven, sumEven

def average(size, sum):
	return (float)(sum)/size


