#write a program that randomly generates the size of 
#the list, in range 3 to 15
#each list element will store the final price 
#for specific item

#for each item we will enter original price
#discount percent and tax
#function price will calculate the final price and
#return it
#in man we will process the list and print the final 
#prices for all items

import random 
def main():
	size = random.randint(3, 15)
	print("size of the list is ", size)
	
	price_list = [0]*size
	for i in range(size):
		original = int(input("enter original price: "))
		discount = int(input("discount percent: "))
		tax = int(input("tax percent: "))

		final_price = price(original, discount, tax)
		price_list[i] = final_price

	print("final prices are: ")
	print(price_list)

def price (original, discount, tax):

	final = (original - original*discount/100)*(1+tax/100)
	return final
main()
