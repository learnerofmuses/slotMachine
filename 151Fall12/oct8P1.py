#write a function that has one formal parameter - int
#function prints EVEN if parameter is even and prints ODD otherwise

#write a program that reads 3 numbers and for each number prints
#even or odd

def even_odd(num):
	
	if (num % 2 == 0):
		print(num, "EVEN")
	else:
		print(num, "ODD")
def main():
	num1=int(input("enter first int "))
	num2=int(input("enter second int "))
	num3=int(input("enter third int "))
	#print(num1)
	even_odd(num1)
	#print(num2)
	even_odd(num2)
	#print(num3)
	even_odd(num3)
main()

#LAB REPORT
#1. Names of ALL functions in your program 
#even_odd, main
#2.Names of formal and actual parameteres for EACH function 
#even_odd formal parameter is num 
#formal parameter is parameter that is used in function definition 
#we have 3 function calls, actual parameters: num1, num2, num3
#3.List of input values you used to test your program
#input: 45 -89 56
#ouput: (45, ODD), (-89, ODD), (56, EVEN) - this is correct output 

