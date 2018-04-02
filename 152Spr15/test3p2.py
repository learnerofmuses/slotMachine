#Discount store sells items on discounted prices. 
#Assume that all numbers are INTEGERS.
#The inventory is stored in the 2D list named inventory in the following 
#way:

#Number of rows = number of items in the store
#Number of columns = 4

#First column - prices of all items
#Second column - discount percent of Category I items
#Third column - discount percent of Category  II items
#Forth column - dicount percent of Categoy III items

#Pay attention, the numbers in 2, 3, and 4 columns are the same for all 
#items

#The discount rule is:
#a. Category I: price of the item less than 5 dollars
#b. Category II: price is between 5 and 9
#c. Category III: items that cost 10 dollars or more 

#Write a functon def final_price_list(inventory, row, col) that has 3 
#parameters - 2D list described above, number of rows and 
#number of columns. Function creates and returns 1D list of final prices 
#for all items after discount is applied. Assume that there 
#is NO TAX.

#Write main to test your function..

#For example, if the inventory 2D list is:
#2  10 30 15
#5  10 30 15
#12 10 30 15
#9  10 30 15

#The function will return the following list:
#[1.8, 3.5, 10.2, 6.3]



