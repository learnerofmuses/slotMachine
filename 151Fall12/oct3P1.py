#name: Tyler
#date: OCT 3 2012
#solution to program 8 from the textbook 
#p. 115 

#we will write one function 
#profit that has two formal parameters
#amount and price
#this function will calculate the profit from
#selling the tickets 

#we write a mian function that will ask user to enter
#the number of tickets for each category (class A $15 per ticket,
#class B $12 per ticket, class C $9 per ticket)
#and prints the profit from each category 

#we will declare three global constants to hold ticket price for 
#each category

A=15
B=12
C=9

def profit(amount, price):
	
	result = amount*price 
	print(result) 
def main():
	#Part I:
	classA = int(input("enter class A number of tickets "))
	classB = int(input("enter class B number of tickets "))
	classC = int(input("enter class C number of tickets "))

	#Part II: function calls
	
	print("the profit from selling class A tickets is ")
	profit(classA, A)
	print("the profit from selling class B tickets is ")
	profit(classB, B)
	print("the profit from selling class C tickets is ")
	profit(classC, C)

main()

