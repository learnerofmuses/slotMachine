#name: Tyler
#date: OCT 1 2012
#Write a function which calculates
#BODY MASS INDEX(BMI) of the person using
#the formula in the book on page 115 in the
#programming exercise 6. Function has 2 
#formal parameters, weight and height of
#three different people and calculates 
#BODY MASS INDEX(BMI) for each person using 
#the function. 

def body(weight, height):
	BMI=(weight * 703)/(height*height)
	print(BMI) 
def main(): 
	#slight modification 
	#calculate (BMI) for 3 different people 

	#Input 
	height1=float(input("please enter your first height "))
	weight1=float(input("please enter your first weight ")) 
	height2=float(input("please enter your second height "))
	weight2=float(input("please enter your second weight "))
	height3=float(input("please enter your third height "))
	weight3=float(input("please enter your third weight "))

	


	print("the BMI for person 1 is")
	body(weight1, height1)
	print("the BMI for person 2 is")
	body(weight2, height2)
	print("the BMI for person 3 is")
	body(weight3, height3)

#Call the main function 

main()
	
