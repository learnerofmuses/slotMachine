#name:Tyler
#date:Nov21 2012

#Function sumInput that has one parameter - the number of input integers. 
#The function inputs integers and finds their sum. USE LOOP FOR in this 
#function. 
#Function productInput that has one parameter - the number of input 
#integers. The function inputs integers and finds their product. USE LOOP 
#WHILE in this function.
#Function average that has NO parameters. The function inputs the series of 
#positive integers. The first zero or negative terminates the input. The 
#function finds the average of the input numbers. In this function you can 
#only use LOOP WHILE. 
#Function menu that has one parameter - choice. The function performs the 
#following: if the choice is 1, user is asked to enter the number of inputs 
#and the function sumInput is called. If the choice is 2, user is asked to 
#enter the number of inputs and the function productInput is called. If the 
#choice is 3, function average is called. For all other choices, function 
#outputs error message. 
#Write main function that reads one integer - user's choice and call 
#function menu. 

def sumInput(num):
	sum = 0 
	count = 0 
	for i in range(num):
		n = int(input(""))
		
		if(n>0):
			count = count + 1
			sum = sum + n
	return sum

def productInput(num):
	product = 1
	count = 0 
	while(num > count):
		n = int(input(""))

		count = count + 1
		product = product * n
	return product

def average():
	sum = 0
	count = 0
	num = int(input("enter a number "))
	while(num <= 0):
		num = int(input(""))
		sum = sum + n
		count = count + 1
	ave = float(sum)/count

	return ave	


def menu(choice):
	if(choice == 1):
		num = int(input("enter number of inputs "))
		while(num<=0):
			print("input is equal or less then 0")
			num = int(input("enter number of inputs "))
		print("processing sum, enter", num, "inputs")
		sumResult = sumInput(num)
		print("sum of inputs is", sumResult)

	elif(choice == 2):
		num = int(input("enter number of inputs "))
		while(num <= 0):
						
			num = int(input("enter number of inputs "))
				
		print("processing product, enter", num, "inputs")
		productResult = productInput(num)
		print("product of the inputs is", productResult)

	elif(choice == 3):
		
		aveResult = average
		print("average of the inputs is")
		
def main():
	choice = int(input("enter your choice "))
	menu(choice)
main()

#LAB REPORT
#choice 1
#input: 5 numbers: 5, 4, 3, 2, 1
#output:15

#choice 2
#input: 3 numbers: 4, 5, 3
#output: 60 
 
#choice 3 
#input: 2 numbers: 12, 2
#output: 7.0

