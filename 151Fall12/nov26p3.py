#write a function that reads 10 ints and returns their average
#write main to test your function 

def ave():
	sum = 0 
	print("enter 10 ints")
	for i in range(10):
		num = int(input(""))
		sum = sum + num

	result = float(sum)/10
	return result 

def main():
	print("the average of 10 inputs is")
	print(ave())
	#different option 
	#res = ave()
	#print(res)

main()

