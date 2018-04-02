#Lab 3 using lists

def main():
	size = int(input("enter number of houses: "))
	price_list = process(size)
	print("the list of purchasing prices is: ")
	print(price_list)

	good, bad = investment(price_list)
	if(len(good)) > 0):
		print("there are", len(good), "houses to buy")
		print("their prices are ")
		print(good)
	else:
		print("there are no good investments")
	if(len(bad) > 0):
		print("there are", len(bad), bad investments")
		print("their prices are ")
		print(bad)
def purchase_price(after_repair_value, repair_expenses):
	price = after_repair_value*75/100 - repair_expenses
	return price

def process(size):
	price = []
	for i in range(size):
		arv= int(input("enter amount you will sell the house after repair: "))
		repair_expenses = int(input("enter repair cost: "))
		
		price_result = purchase_price(arv, repair_expenses)
		price.append(price_result)

	return price

def investment(price):
	good_investment = []
	bad_investment = []
	
	for i in range(len(price)):
		current_value = int(input("enter the current value of the house: "))
		if (current_value > price[i]):
			bad_investment.append(price[i])
		else:
			good_investment.append(price[i])
	return good_investment, bad_investment


main()
