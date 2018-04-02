#1. Function pass_fail_A that has one parameter - number of students in 
#class. The function reads students grades and returns the number of 
#students who failed the class, the number of studenst who passed the 
#class, the number of students who got grade A, the sum of passing grades, 
#the sum of failing grades, and the sum of A grades.
#2. Function average that has two parameters, sum of the grades and the 
#number of the grades. The function returns the average grade. 

def pass_fail_A(num):
	passing = 0 
	fail = 0
	gradeA = 0 
	sumPass = 0 
	sumFail = 0
	sumGrade_A = 0
	print("enter", num, "students ")
	for i in range(num):
		grade = int(input(" "))
		if(grade >= 91): 
			passing +=1 
			gradeA +=1 
			sumPass +=grade
			sumGrade_A +=grade
		elif(grade >= 61):
			sumPass +=grade
			passing +=1
		else:
			fail +=1
			sumFail +=grade
		
	return passing, sumPass, fail, sumFail, gradeA, sumGrade_A

def average(numGrades, sum):
	return (float)(sum)/numGrades  
			
