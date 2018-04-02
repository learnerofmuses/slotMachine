#name:Tyler
#date:OCT 22,2012

#Write a program that calculates the final grade in TWO different courses. 
#First course, final grade is average of midterm and homework grade.
#Second course, final grade is 15% of quizzes, 35% of homework, and
#50% of midterm. Write separate function for each course. Write main 
#function that first reads one integer, 1 - indicates to calculate 
#grade  in course 1 and number 2 - indicates to calculate the grade in 
#course 2. Program reads all required inputs, 2 grades for first course
#and 3 grades for second course.Two functions you write to output final 
#grade for course 1 or course 2 based on first input.Input grades are 
#INTEGERS, but final grade must be FLOAT.Display final grades with 
#3 digits after decimal point.Use GLOBAL CONSTANTS for percent values.
#Check validity of input - must be done in main.Output error message if 
#first input number is not correct choice(1 or 2). 

quizzes = 0.15
homework = 0.35
midterm = 0.50
def course_1(midterm, homework):

	FC = (midterm + homework)/ 2.0
	print(FC)
	
def course_2(quizzes, homework, midterm):

	SC = (midterm + quizzes + homework)/ 3.0
	print(SC)

def main():

	homework1=int(input("enter homework grade for first course "))
	homework2=int(input("enter homework grade for second course "))
	midterm1=int(input("enter your midterm grade for first course "))
	midterm2=int(input("enter your midterm grade for second course "))
	quizzes2=int(input("enter your quiz grade for second course "))
	print("the final grade for course 1 is")
	course_1(homework1, midterm1)
	print("the final grade for course 2 is")
	course_2(homework2, midterm2, quizzes2)
	
main()

#LAB REPORT
#1. NAME OF FUNCTIONS ARE: course_1 course_2 and main
#2. formal parameters are homework1 homework2 midterm1 midterm2 and
#quizzes2 
#3.Input values used for homework(78,97)
#4.Input values used for midterm(89,83)
#5.Input values used for quiz(90)
#6.Output for course 1 is 71.8
#7. Output for course 2 is 88.95

