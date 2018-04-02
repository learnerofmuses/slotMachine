#Tyler
#Nov 26 2012
#write a program that gives simple math quizzes. The program should 
#display two random numbers that are to be added.
#The program should allow the student to enter the answer. If the answer
#is correct, a message of congratulations should be displayed. If the 
#answer is incorrect, a message showing the correct answer should be 
#displayed.

import random
		
def main(): 
	a = random.randrange(1, 1000)
	b = random.randrange(1, 1000)
	print(a,b)
	sum = a + b
	user = int(input("enter the answer "))
	if(sum == user):
		
		print("Congratulations")
	else:
		print("incorrect answer")
		print("the correct answer is") 		

main()
