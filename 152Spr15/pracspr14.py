#working with lists
SIZE = 5
import random
def main():
	num = [0]*SIZE
	num1 = [0]*SIZE

	print("print list using name of the list ")
	print(num)
	print("the length of the list is ")
	print(len(num))

	print("print list using loop  ")
	for i in num:
		print(i)

	print("print list using loop and index ")
	for i in range(SIZE):
		print(num[i])
	print("the values of list could be changed ")
	num[2] = -5
	print("the list after change is")
	print(num)

	print("we will assign random number for each element ")
	for i in range(SIZE):
		num[i]=random.randint(0,100)
		num1[i]=random.randint(-100, -1)

	print("the new lists are")
	print("num is")
	print(num)
	print("num1 is")
	print(num1)

	print("concatenation of both lists")
	num2 = num+num1
	print(num2)
	print("the length of concatenated list is ")
	print(len(num2))
main()
