#The winter sale in some store has the following rules: if the original 
#price of the 
#item is 50 dollars or less, the item has 20% discount, otherwise, the 
#item has 50% discount.

#The program randonly generates original prices of the items and stores
#the prices in the list. We will assume that prices are INTEGERS between 
#25 and 75 (THIS 
#PART IS DONE FOR YOU!). 

#The program creates TWO new lists: 
#1. list of discounted prices for all items. 
#2. list of all discounts, as integers. 
#The program finds: 
#1. average original price
#2. average  discounted price
#3. average discount

#Write function average that has ONE paremeter - list. The function 
#finds and returns an average of list elements.

#Write function process that has ONE paremeter - list of original 
#prices. The 
#function creates amd returns TWO new lists: list of dicounted prices 
#and list of discounts

#Complete the main to test your function
 
#Example:
#size 5, original_price=[26, 50, 70, 56, 48]
#discount=[20, 20, 50, 50, 20]
#discount_price=[20.8, 40, 35, 28, 38.4]
#average_original=50.0
#average_discount_price=32.44
#average_discount_percent=32  

import random 

def make_list(size, min_limit, max_limit):
	my_list = []
	for i in range(size):
		n=random.randint(min_limit, max_limit)
		my_list.append(n)
	return my_list

#def average(my_list):
	#sum = 0 
	#length = len(my_list) 

	
def process(my_list):
	discount = [] 
	trs = my_list[i] 
	wu = 0 
	for i in range(len(my_list):
		if(trs<=50):
			wu = trs*(trs*.20)
			discount.append(wu)
		else:
			wu = trs*(trs*.50)		
			discount.append(wu)
	return discount
		
		

def main():

	size = int(input("enter the number of items in the store "))
	orginal_price = make_list(size, 25, 75)
	print("original prices ")
	print(original_price)
	
	discount = process(my_list)
	print(discount)
main()
