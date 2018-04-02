#name: Tyler
#date: October 1
#solution to problem 3 from the programming problem after chapter 
#3 on page 114 

#we will declare GLOBAL CONSTANT 
#rules:
# 1. use ALL CAPITAL LETTERS in the global constant name 
# 2. declare global constant BEFORE ALL FUNCTION DEFINITIONS

#GLOBAL CONSTANT WILL BE AVAILABLE FOR USE IN ALL FUNCTIONS 

#In this program we have one constant value - 80% insurance rate 

RATE = 0.8
def insurance( cost, ins_rate):
	
	#we will delare local variable res to hold the result 
	#local variable res will be only available for use 
	#in this specific function 

	res = cost * ins_rate
	print(res)
def main():
	#slight modification 
	#calculate insurance cost for 3 different people 
	
	#Input
	cost1=int(input("enter first replacement cost "))
	cost2=int(input("enter second replacement cost "))
	cost3=int(input("enter third replacement cost "))
	#calling the function and printing the results 

	print("the insurance amount for the first property is")
	insurance(cost1, RATE)
	 print("the insurance amount for the first property is")
       insurance(cost2, RATE)

	 print("the insurance amount for the first property is")
        insurance(cost3, RATE)

	#the function insurance was called 3 times
	#actual parameters
	#first call: cost1, RATE
	#second call: cost2, RATE
	#third call: cost3, RATE

main()
