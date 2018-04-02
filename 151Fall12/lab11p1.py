#Tyler
#Dec 3 2012
#Function sumNeg that has one parameter - the number of input integers. The 
#function inputs integers, and finds and RETURNs the sum of the negative 
#inputs. If there are no negative inputs, the function returns 0.
#USE LOOP FOR in this function. 
#Function averageEven that has NO parameters. The function inputs the 
#series of positive integers. The first zero or negative terminates the 
#input. The function finds and RETURNs the average of the EVEN input 
#numbers. If there are no even inputs, the function returns -1.
#In this function you can only use LOOP WHILE. 
#Function menu that has one parameter - choice. The function performs the 
#following: if the choice is 1, user is asked to enter the number of inputs 
#and the function sumNeg is called. If the choice is 2, function average is 
#called. For all other choices, function outputs error message. 
#Write main function that reads one integer - user's choice and call 
#function menu.

def sumNeg(num):
	sumNeg = 0 
	countNeg = 0 
	for i in range(num):
		n = int(input(""))
		sumNeg = sumNeg + n	 
		countNeg = countNeg + 1
	if(sumNeg <= 0):
		
		
		result = sumNeg
	else:
		result = 0

	return result 

def averageEven():
	sumEven = 0
	countEven = 0	
	n = int(input(""))
	while(n>0):
		d = n % 10
		if(d % 2 == 0):
			sumEven = sumEven + d
			countEven = countEven + 1
		n = int(input(""))
	if(countEven > 0):
		result = float(sumEven)/countEven
	else:
		result = -1
	return result
		
def menu(choice):
	if(choice == 1):
		num = int(input("enter number of inputs "))		

		while(num <= 0):
			print("input is less than or equal to 0")
			num = int(input("enter number of inputs "))
		print("processing sum neg, enter", num, "inputs")
		res = sumNeg(num)
		print("sum of negative nums is", res)
	elif(choice == 2):
		print("enter series of positive inputs")
		res = averageEven()
		if(res == -1):
			print("no even inputs", res)
		else:
			print("average of the even inputs is", res)
	else:
		print("error")
			
def main():
	choice = int(input("user enter choice "))
	menu(choice)
main()

#LAB REPORT
#CHOICE 1
#input1: 4 negative inputs: -4 -3 -2 -1
#output1: returns sumNeg -10 

#input2: 4 positive inputs: 2 3 4 5
#output2: returns 0

#CHOICE 2
#input1: 9 inputs: 1 2 3 4 5 6 7 8 0
#first 0 or negative number terminates input
#output1: average of the even inputs is, 5.0 

#input2: 5 inputs: 3 3 5 7 0
#first 0 or negative number terminates input
#output2: no even inputs, returns -1  
