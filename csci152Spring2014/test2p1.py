#For the program written below, give an example of input to receive the 
#following output:

#25
#[8, 7, 6, 4]


def main():
	my_list=[[ 0 for i in range(4)] for j in range(3)]
	game = 0 
	for i in range(3):
		for j in range(4):
			my_list[i][j]=int(input("enter number "))
			game = game + my_list[i][j]
	print(game)
	fun=[0]*4
	for j in range(4):
		for i in range(3):
			fun[j]=fun[j]+my_list[i][j]
		
	print(fun)	
	
main()

