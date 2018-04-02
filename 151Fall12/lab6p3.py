#name:Tyler
#date:OCT22,2012

#write a program that reads TWO exit numbers and outputs the speed limit
#for each exit. Program must check if exit is even or odd and call an
#appropriate function. If input is outside of exit range, your 
#program must print error message. 
#Ex. Input is 7, 21 then output is 65mph, invalid input.
#If input is 10, 11 then output is 55mph, 50 mph.

def highway1(exit):
	if(exit>=18) and (exit <= 20):
		print("Your speed is 50 mph")
	elif(exit>=8) and (exit <= 60):
		print("Your speed is 55 mph")
	elif(exit>=2) and (exit <= 6):
		print("Your speed is 65 mph")
	else:
		print("ERROR")
def highway2(exit):
	if (exit>=15) and (exit <= 19):
		print("Your speed is 45 mph")
	elif(exit>=11) and (exit <= 13):
		print("Your speed is 50 mph")
	elif(exit>=5) and (exit <= 9):
		print("Your speed is 65 mph")
	elif(exit>=1) and (exit <= 3):
		print("Your speed is 55 mph")
	else:
		print("ERROR")
	
def main():
	exit1=int(input("enter the first exit on highway1 "))
	exit2=int(input("enter the second exit on highway1 "))
	
	print("The speed limit on highway 1 is")
	highway1(exit1)
	print("The speed limit on highway 1 is")
	highway1(exit2)
	
	exit1=int(input("enter the first exit on highway 2 "))
	exit2=int(input("enter the second exit on highway 2 "))
	
	print("The speed limit on highway 2 is")
	highway2(exit1)
	print("The speed limit on highway 2 is")
	highway2(exit2)
main()

#LAB REPORT
#there are three functions highway1 highway 2 and main
#formal parameters for highway1 and highway2 is exit
#main has no functions
#actual parameters for highway1 and highway2 are exit1 and exit2
#Inputs for highway1 are: 4-exit1, 2-exit2
#Outputs are: 65 mph-exit1, 65mph-exit2
#Inputs for highway2 are: 9-exit1, 3-exit2
#Ouputs are: 65mph-exit1, 55mph-exit2

