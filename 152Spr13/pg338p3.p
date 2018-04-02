#Tyler Scott
#Jan 30 

import pg338p1
import pg338p2

def main():

	print("Part I, Total Sales")
	print("Part II, Lottery Draw")

	choice = int(input(" "))
	
	if(choice == 1):
		i = 1
		my_list = []
		while(i <=7):
			sales = int(input("what are the sales for the day?"))		
			my_list.append(sales)
			i = i + 1
		total = pg338p1.my_list
		print(total)
main()
