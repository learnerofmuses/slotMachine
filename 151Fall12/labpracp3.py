#Tyler
#Nov 26 2012
#write a function named maximum that accepts two integer values as 
#arguments and returns the value that is the greater of the two. 
#Use the function in a program that prompts the user to enter two integer
#values. The program should display the value that is the greater of the
#two.

def maximum(num1, num2):
	if(num1>num2):
		max = num1
	else:
		max = num2

	return max
	
	
def main():
	num1= int(input("enter first number "))
	num2 = int(input("enter second number "))	
	result = maximum(num1, num2)
	print(result)
main()
