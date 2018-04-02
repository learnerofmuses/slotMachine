#write a program that reads 10 integers and 
#finds the amount, sum and average of numbers divisible by 7 

def main():
	
	count7 = 0
	sum7 = 0
	
	for i in range(10):
		num = int(input("enter int "))
		if (num%7 == 0):
			sum7=sum7+ num 
			count7 = count7 + 1

	if(count7>0):
		ave7=float(sum7)/count7
		print("there are ", count7, "divisible by 7")
		print("their sum is", sum7)
		print("their average is", ave7)
	else:
		print("no divisible by 7")
main()
