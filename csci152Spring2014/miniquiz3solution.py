#mini quiz 3 solution 

import random 

def main():
	size = int(input("enter size of the store "))
	price = make_list(size)
	print("list of all prices is ")
	print(price)
	dollar,fivebelow, general= separate(price)

	print("dollar prices")
	print(dollar)

	print("five below prices")
	print(fivebelow)
	
	print("general section")
	print(general)

	len_list= []
	len_list.append(len(dollar))
	len_list.append(len(fivebelow))
	len_list.append(len(general))

	print("list of lengths ")
	print(len_list)
def make_list(size):
	price= []
	for i in range(size):
		price.append(random.uniform(0,6))

	#price = [0]*size
	#for i in range(size):
	#	price[i] = random.randint(0,60
	
	return price
def separate(price):
	dollar = []
	fivebelow= []
	general = []
	for i in range(len(price)):
		if(price[i]<1):
			dollar.append(price[i])
		elif(price[i]>=1 and price[i]<=5
			fivebelow.append(price[i])
		else:
			general.append(price[i])
	return dollar, fivebelow, general 
main()
