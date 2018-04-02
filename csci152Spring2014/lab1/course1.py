#1. Function pass_fail that has one parameter - number of students in 
#class. The function reads students grades and returns the number of 
#students who failed the class, the number of students who passed the 
#class, the sum of the passing grades, and the sum of the failing grades.
#2. Function average that has two parameters, sum of the grades and the 
#number of the grades. The function returns the average grade.




def pass_fail(num):
	passing = 0 
	fail = 0
	sumPass = 0 
	sumFail = 0  
	print("enter", num, "students ")
	for i in range(num):
		grade = int(input(" "))
		if(grade >= 61):
			sumPass+=grade
			passing+=1
			
		else:
			sumFail+=grade
			fail+=1
			
	return passing, sumPass,fail, sumFail 				
			 
def average(num, sum):
	return (float)(sum)/num 



