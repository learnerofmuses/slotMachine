#write a program that reads 3 numerical grades 
#and for each grade convert it to letter grade using the 
#following table 
#100 - 90 A
#89 - 80 B
#79 - 70 C
#69 - 60 D
#below 60 F

#less than 0 or greater than 100 - error message

def letter_grade(grade):
	
	if(grade<0):
		print("error")
	elif(grade > 100):
		print("error")
	elif(grade>=90):
		print("A")
	elif(grade>=80):
		print("B")
	elif(grade>=70):
		print("C")
	elif(grade>=60):
		print("D")
	else:
		print("F")
def main():
	grade1=int(input("enter grade for first student "))
	grade2=int(input("enter grade for second student "))
	grade3=int(input("enter grade for third student "))
	print("letter grade for first student")
	letter_grade(grade1)
	print("letter grade for second student")
	letter_grade(grade2)
	print("letter grade for third student")
	letter_grade(grade3)
main()
#LAB REPORT
#there are 7 choices and for testing we have to check all of them 
#we have to run the program at least 3 times to cover all choices
#input: 90 89 67
#output: A B D
#input: -90 102 56
#output: error error F
#input: 75 91 87
#output: C A B

#based on the conversion table our program outputs correct results
