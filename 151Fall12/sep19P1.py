#name: Tyler
#date: Sep 19 
#write the program that asks user to input the price 
#of the item and the state TAX and calculate the final price 

#assume that the tax is float number 
#assume that the price is integer

#Part I: Input
price = int(input("please enter price "))
tax = float(input("please enter tax "))

#Part II: Calculations: 

total = price*tax + price 
#different way to write: total = price*(1+tax)

#Part III: Results

print("original price before tax is ")
print(price)
print("state tax is ")
print(tax)
print("the total price is ")
print(format(total, '.2f'))

 


