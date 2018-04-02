#Write a function average that reads NUM integers and returns their 
#average. Write a function positive that reads NUM integers and returns 
#the number of positive numbers among the input. In case there are no 
#positive numbers, function returns 0. Write a function even that reads 
#NUM positive integers and returns the average of the even numbers. In 
#case there are no even positive numbers, function returns 0. Write a 
#function word that reads NUM words and retunrs the number of "python" 
#words. In all functions, NUM - is the parameter for the function that 
#indicates the size of the input. 
#Write a function menu that accepts one integer parameter. For function 
#menu, 1 - indicates to call function average, 2 - indicates to call 
#function positive, 3 - indicates to call to fucntion even, 4 - indicates 
#to call function word. All other choices are not valid. In function main, 
#ask user to enter one integer and call function menu with user's choice. 

def average(num):
	sum = 0 
	
	for i in range(num):
		n = int(input(""))
		sum = sum + n
	ave = float(sum)/num
	return ave
def positive(num): 
	countPos = 0 
	for i in range(num):
		n = int(input(""))
		if(n>0):
			countPos = countPos + 1
		
		return countPos	
def even(n):
	if(n%2 == 0):
		res = True
	else:
		res = False
	
	return res

def evenAve(num):
	sumEven = 0 
	countEven = 0 
	for i in range(num):
		n = int(input(""))
		if(even(n)):
			sumEven = sumEven + n
			countEven = countEven + 1

	if(countEven>0):
		ave = float(sumEven)/countEven
	else:
		ave = 0 
	
	return ave
def menu(choice):
	if(choice==1):
		num = int(input("input size "))
		while(num<=0):
			print("try again")
			num = int(input("input size "))
		print("processing average, enter", num, "inputs")
		aveResult = average(num)
		print("average of inputs is", aveResult)

	elif(choice == 2):
		num = int(input("input size "))
               	while(num<=0):
                	print("try again")
                        num = int(input("input size "))
               	print("processing count positive inputs")
		print("enter", num, "inputs")
		resultCountPositive = positive(num)
		if(resultCountPositive == 0):
			print("no positive inputs")
		else:
			print("there are", resultCountPositive, "positive inputs")
	elif(choice==3):
		num = int(input("input size "))
                while(num<=0):
                	print("try again")
                        num = int(input("input size "))
                print("processing average even inputs")
		print("enter", num, "inputs")
		res = evenAve(num)
		if(res == 0):
			print("no evens")
		else:
			print("average of evens is")
			print(res)
	else:
		print("invalid input")
def main():
	choice = int(input("enter your choice "))
	menu(choice)
main()
