#Write a menu function that will allow user to choose between two courses. 
#If the choice is 1, the user will be asked to enter the number of 
#students in the first class and to find the number of failing grades, the number 
#of passing grades, the average failing grade and the average passing 
#grade. PAY ATTENTION: the program must output the appropriate message in 
#case and there are no passing grades or there are no failing grades.
#If the choice is 2, the user will be asked to enter the number of 
#students in the second class and find the number of failing grades, the 
#number of passing grades, the number of A's, the average failing grade, 
#the average passing grade, and the average A grade. PAY ATTENTION: the 
#program must output the appropriate message in case, and there are no 
#passing grades or there are no failing grades or there are no A's.
#The program must output "invalid choice" message for choices that are not 
#1 or 2. Also, check the validity of the input for the number of students 
#in each class. 


import course1
import course2
def main():
	print("enter choice: 1 for course1 and 2 for course2 ")
	choice = int(input(" "))
	if(choice == 1):
		num = int(input("enter the number of students "))
		if(num > 0):
			p, sP, f, sF = course1.pass_fail(num)
			if(f > 0):
				ave = course1.average(f, sF)
				print("there are", f, "fails")
				print("their sum is ", sF)
				print("their average is", ave)
			else:
				print("there are no failing grades")
			if(p > 0):
				ave = course1.average(p, sP)
				print("there are", p, "passes")
				print("their sum is ", sP)
				print("their average is ", ave)
			else:
				print("there are no passing grades")
		else:
			print("number of students invalid")
	elif(choice == 2):
		num = int(input("enter the number of students "))
		if(num > 0):
			p, sP,f, sF, gradeA, sumGrade_A = course2.pass_fail_A(num)
			if(f > 0):
				ave = course2.average(f, sF)
				print("there are", f, "fails")
				print("their sum is ", sF)
				print("their average is ", ave)
			else:
				print("there are no failing grades")

			if(p > 0):
				ave = course2.average(p, sP)
				print("there are", p, "passes")
				print("their sum is ", sP)
				print("their average is ", ave)
			else:
				print("there are no passing grades")
			if(gradeA > 0):
				ave = course2.average(gradeA, sumGrade_A)
				print("there are", gradeA, "grades")
				print("their sum is ", sumGrade_A)
				print("their average is ", ave)
			else:
				print("there are no A in the class")
main()
				
			
				
