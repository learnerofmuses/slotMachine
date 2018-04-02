#write a function max that has 3 formal 
#parameters: integers  n1, n2, n3. The function finds
#and prints the largest number among n1, n2 and n3

#write a program that reads 6 integers 
#and finds the maximal value for the first three numbers and
#for the second three numbers. You have to use function max to do 
#so

#Algorithm:
#First, find the max between n1 and n2
#second compare max to n3 and update it if n3 is larger
def max(n1, n2, n3):
	if ( n1 < n2):
		max = n2
	else:
		max = n1

	if (max < n3):
		max = n3

	print(max)

def main():
	x = int(input("enter first int "))
	y = int(input("enter second int "))
	z = int(input("enter third int "))
	print("the maximal value among ", x, y, z)
	max(x,y,z)
	x = int(input("enter first int "))
        y = int(input("enter second int "))
        z = int(input("enter third int "))
        print("the maximal value among ", x, y, z)
        max(x,y,z)
main()
#LAB REPORT 
#2 functions main and max
#main - no parameters
#max has 3 parameters
#formal parameters for max are n1, n2, n3
#actual parameters for max are x, y, z

#TESTING
#WE MUST RUN OUR PROGRAM AT LEAST 3 TIMES
#TO COVER ALL POSSIBLE ORDERS OF 3 NUMBERS
#THERE ARE 6 POSSIBLE ORDERS, AND EACH INPUT WILL COVER 2
#POSSIBILITIES
#INPUT 1
#1 2 3
#1 3 2
#INPUT 2
#2 1 3
#2 3 1
#INPUT 3 
#3 1 2
#3 2 1

