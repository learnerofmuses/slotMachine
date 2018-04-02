#write a program that generates 10 random numbers between 1 and 100
#each number represents the grade, and the program counts
#the number of passing grades and the average passing grade
#passing grade - grade is larger or equal 60

import random
 
def passCourse(students):
	countPass = 0 
	sumPass = 0 
	for i in range(students):
		grade = random.randit(1,100)
		print(grade)
		if(grade >=60):
			countPass = countPass + 1
			sumPass = sumPass + grade
		
	if (countPass > 0):
		avePass = float (sumPass)/countPass
		print("output is")
		print("there are", countPass, "students passed the course")	
		print("the average passing grade is ", avePass)
	else:
		print("no passing grades")

def main():
	passCourse(10)

main()
