#write a function divThree that has one parameter
#function return True if parameter is divisible by 3
#and False otherwise

#write main that reads a sequence of non-zero integers
#first zero will terminate the input
#for each number the program outputs, YES if the numbers
#divisible by 3 and NO otherwise
#program also counts the number of inputs that are divisible by 3
#their sum and average

def divThree(num):
	if(num%3 == 0):
		result = True
	else: 
		result = False
	
	return result
	
def main():
	
	num = int(input("enter int "))
	sum = 0
	count = 0
	while(num != 0):
		if(divThree(num)):
			print("YES")
			count = count + 1
			sum = sum + 1
		else:
			print("NO")

		num = int(input("enter int "))
	if (count > 0):
			ave = float(sum)/count
			print("there are ", count, "inputs div by 3")
			print("their sum is", sum)
			print("their average is", ave)
	else:
		print("no inputs divisible by 3")
main()
