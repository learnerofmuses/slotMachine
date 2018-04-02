import random

def main():
	size = int(input("enter the size of the list: "))
	
	result = separate(price_list)
	print(result)
	dL, fbL, gaL = separate(price_list)
	if(dL >= .01 and dL <= 1):
		print("list for dollar section", dL)
	else:
		print("nothing available of these prices in this section")

	if(fbL >= 2 and fbL <= 5):
		print("list for five below section", fbL)
	else:
		print("nothing available of these prices in this section")
	if(gaL >= 6 and gaL <= 500):
		print("list for general area section", gaL)
	else:
		print("nothing available of these prices in this section") 

def separate(price_list):
	dollar_list = []
	five_below_list = []
	gen_area_list = []

	for i in range(size):
		dollar_list.append(random.uniform(.01, 1))
		five_below_list.append(random.uniform(1, 5))
		gen_area_list.append(random.uniform(6, 500))
	return dollar_list, five_below_list, gen_area_list

main()
