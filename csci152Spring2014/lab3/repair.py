#Write a function def purchase_price(ARV, repair_expenses) that has 2 
#parameters:

#    ARV is after_repair_value, is the price that you can sell your home 
#AFTER it is all fixed up
#    repair_expenses - amount of dollars to repair the house

#    The function will use the the formula written below to calculate 
#the purchase price:

#    purchase_price = 75% * (after_repair_value) - repair_expenses

#    The function returns the purchase price 

#Write a function def process(size), size is the number of houses the 
#customer consider for purchasing. The function reads after_repair_value 
#and repair_expenses for each house, and the current market price for 
#the house. The function then calls function purchase_price to calculate 
#the price that investor should pay for the house to make it worthwhile 
#investment. The function returns the number of houses that worthwhile 
#investment and the number of houses that priced too high on the current 
#market. FOR TESTING PURPOSES, PRINT the purchasing price for EACH house
#Write main program that randomly generates the number of houses 
#customer cosider for investment, assume that the size is between 3 and 
#15 and call function process to find the number of houses that 
#worthwhile an investment and the number of houses that are priced too 
#hight on the current market.
#TEST YOUR PROGRAM and document INPUT/OUTPUT in the comment part before 
#your submission. 

import random

def purchase_price(AVR, repair_expenses):
	purchase = .75*(AVR)-repair_expenses
	return purchase

def process(size):
	
	for i in range(size):
		countB = 0
		countG = 0
		arv = int(input("enter the after repair value: "))
        	RE = int(input("enter the repair expenses: "))
        	cmp = int(input("the current market price for this house is: "))

        	purchase = purchase_price(arv, RE)
		print(purchase)
		if(purchase < cmp):
			print("this house's market value is too high")
			countB+=1
		else:
			print("this is a worthwhile investment")	
			countG+=1
	return 	countB, countG

def main():
	size = random.randint(3, 15)
	
	print(process(size))	
main()

#COMMENT PART
#enter the after repair value: 220000
#enter the repair expenses: 25000
#the current market price for this house is: 160000
#140000.0
#this house's market value is too high
#enter the after repair value: 200000
#enter the repair expenses: 20000
#the current market price for this house is: 125000
#130000.0
#this is a worthwhile investment
#enter the after repair value: 185999
#enter the repair expenses: 15000
#the current market price for this house is: 124000
#124499.25
#this is a worthwhile investment
#enter the after repair value: 500000
#enter the repair expenses: 100000
#the current market price for this house is: 450000
#275000.0
#this house's market value is too high
#enter the after repair value: 25000
#enter the repair expenses: 1000
#the current market price for this house is: 13000
#17750.0
#this is a worthwhile investment
#enter the after repair value: 1000
#enter the repair expenses: 450
#the current market price for this house is: 850
#300.0
#this house's market value is too high
#enter the after repair value: 500
#enter the repair expenses: 100
#the current market price for this house is: 350
#275.0
#this house's market value is too high
#enter the after repair value: 100000000
#enter the repair expenses: 230000 
#the current market price for this house is: 8500000
#74770000.0
#this is a worthwhile investment
(0, 1)


