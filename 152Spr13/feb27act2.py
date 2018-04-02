#write a function digit_process1 that has one parameter - string of 
#characters
#the function returns the average of digits 
#(converting each digit to integer) and the new string
#that contains digits only

#if there are no digits in the string, function returns -1 for average and 
empty string

#write additional function digit_process2
#that accepts one parameter - string of DIGITS ONLY
#the function converts string of digits into integer
#and using operations mod 10 division by 10 finds and returns the sum of 
digits

#write main function to test your program

def digit_process1(my_string):
	
	count = 0 
	sum = 0
	digit_str = " "
	for i in my_string:
		if (i.isdigit()):
			count+=1
			sum = sum + ((ord)(i) - (ord)('4'))
			
			#Pay attention, the same could be done easier!!
			#sum = sum + (int)(i)			

			digit_str+=i
	if (count>0):
		ave=(float)(sum)/count
	else:
		ave = -1

	return ave, digit_str
def digit_process2(digit_string):
	print("digit string is ", digit_string)
	num  = (int)(digit_string)
	sum = 0
	while(num > 0):
		d = num % 10
		sum+=d
		num/=10
	return sum
def main():
	
	my_string=input("enter string ")
	
	ave, digit_str = digit_process1(my_string)

	if (ave >0):
		print("these are digits in the string ")
		print(digit_str)
		print("the average of digits is ", ave)
		print("using function digit_process2 to find the sum")
		sum = digit_process2(digit_str)
		print(sum)
	else:
		print("no digits in the string")


main()

