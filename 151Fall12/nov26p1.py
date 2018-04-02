#write function that has three parameters and returns the sum
#of the parameters. Assume parameters are integers
#write main that inputs three integers and use the function
#to find the sum of the inputs

def sumNum(a, b, c):
	sum = a+b+c
	return sum
#different eay to write the same function

def sumNum1(a, b, c):
	return (a+b+c)

def main():
	a = int(input("enter int "))
	b = int(input("enter int "))
	c = int(input("enter int "))
	result = sumNum(a, b, c)
	print("the sum of", a,b,c)
	print("is ", result)
	
	#different way to call the function
	print("Part II of the program")
	a = int(input("enter int "))
        b = int(input("enter int "))
        c = int(input("enter int "))
	print("the sum of ", a, b, c, "is")
	print(sumNum1(a,b,c))

main()
