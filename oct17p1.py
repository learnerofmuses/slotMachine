#write a function that has 2 parameters
#if both parameters are even, the function prints "BOTH EVEN"
#if both parameters are odd, the function prints "BOTH ODDS"
#otherwise, the function prints "ONE EVEN ONE ODD"

#write s program that reads 2 integers and checks their even/odd status
#using the function 

def even_odd(num1, num2):
	
	if((num1 % num2 == 0) and (num2 % 2 == 0)):
		print("BOTH EVEN")
	elif((num1 % 2 != 0) and (num2 % 2 != 0)):
		print("BOTH ODD")
	else:
		print("ONE EVEN ONE ODD")
def main():
	num1 = int(input("enter first int "))
	num2 = int(input("enter second int "))
	print("The results are ")
	even_odd(num1, num2)
main()
#LAB REPORT
#TESTING: must run your program at least 4 times to cover all options
#use negative positive and zero

#12 24 BOTH EVEN
#0 0 BOTH EVEN
#12 -6 BOTH EVEN

#13 -55 BOTH ODD

#12 33 ONE EVEN ONE ODD
#33 12 ONE EVEN ONE ODD
