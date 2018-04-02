#This program will process grades for the group of students. The program 
#will ask user to enter the number of students in the group, and the 
#number of courses each student takes in specific semester. Assume, that 
#all students take the same number of courses. The program will ask user 
#to enter final grade for each course for each student. All grades will 
#be stored in 2-D list. One row of 2-D list stores grades for one 
#student.

#For example, if there are 3 students in the group and each student 
#takes 2 courses, and the input grades are: 90 67 for first student, 99 56 for 
#second student, and 78 67 for third student, the 2-D list of grades 
#will be as follows:

#90 67
#99 56
#78 67

#ASSUME THAT INPUT IS VALID. NO NEED TO CHECK VALIDITY OF THE INPUT.

#Write the following functions:

#def make_2d_list(row, col) - creates 2-d list of grades from user 
#input and returns the list

#def ave(list, row, col) - finds and returns the average of all 
#grades for all students in the group

#dev max(list, row, col) - finds and returns the maximal grade among 
#all grades for all students, and the position of the max grade in the 
#2-d list (i and j). (in case there are more than one appearance of max 
#value, return only one instance of i and j)

#def ave_grade(list, row, col) - finds and returns the ONE 
#dimensional list of averages PER student and PER course.

#main function that inputs number of students in the group and 
#number of courses, creates a 2-d list of grades, finds the average 
#grade for all students in the group, finds the maximal grade among all 
#students in the group and its position, finds the list of averages per 
#student, finds the STUDENT index who got a highest average (If there 
#are several students(courses) with the same highest average, you only 
#need to find ONE index). Use appropriate function for each task 


def make_2d_list(row, col):
		grades=[[0 for i in range(col)]for j in range(row)]
		for i in range(row):
			for j in range(col):
				grades[i][j]=int(input("enter grade: "))
	
		return grades

def ave(list, row, col):
	sum = 0 
	for i in range(row):
		for j in range(col):
			sum+=list[i][j]
	return sum/(row*col)

def max(list, row, col):
	max_grade=list[0][0]
	max_i=0
	max_j=0

	for i in range(row):
		for j in range(col):
			if(list[i][j]>max_grade):
				max_grade=list[i][j]
				max_i=i
				max_j=j
	
	return max_grade, max_i, max_j

def ave_grade(list, row, col):
	ave_per_course=[0]*col
	ave_per_st=[0]*row
	
	
	for i in range(row):
		sum = 0 
		for j in range(col):
			sum=sum+list[i][j]
		ave_per_st[i]=sum/col
	
	
	for j in range(col):
		sum = 0 
		for i in range(row):
			sum=sum+list[i][j]
		ave_per_course[j]=sum/row
	
	return ave_per_course, ave_per_st

def main():
	row=int(input("number of students: "))
	col=int(input("number of courses: "))
	grades = make_2d_list(row, col)
	ave_res = ave(grades, row, col)
	max_grade, max_i, max_j=max(grades, row, col)
	ave_course, ave_stu=ave_grade(grades, row, col)
	for i in range(row):
		print(grades[i])
	
	print("average grade ", ave_res)
	print("max_values", max_grade, max_i+1, max_j+1)
	print("averages per course: ")
	print(ave_course)
	print("averages per student: ")
	print(ave_stu)

main()	
