#Write a program that asks user to enter the number of family members with 
#Facebook account, their names, and the number of hours they spend on 
#Facebook per day during the weekdays. The program finds the total number 
#of hours per family member and the family member who spend the most time 
#on Facebook. Store hours in 2-d list. One rows stores hours for one 
#family member. The number of rows is the number of family members, the 
#number of columns is 5 in our example (there are 5 weekdays). Store 
#family names in additional 1-d list. 

def main():
	family=int(input("number of family members: "))
	names = []
	for i in range(family):
		name = input("enter the family name ")
		names.append(name)
		
	hours = [[0 for i in range(5)] for j in range(family)]
	for i in range(family):
		print("enter hours for ", names[i])
		for j in range(5):
			hours[i][j]=int(input("enter hours: "))

	print("family with Facebook")
	print(names)
	print("hours on Facebook")
	for i in range(family):
		print(name[i], hours[i])
	sumHours = total(hours, family, 5)
	print("names, hours and totals ")
	for i in range(family):
		print(names[i], sumHours[i], hours[i])
		
	print("list of totals ")
	print(sumHours)

	maxHours = max(sumHours)
	print("maximal total is: ", maxHours)
	indexMax = sumHours.index(maxHours)
	print("the person who spends too much time on Facebook is:", names[indexMax]

	print("full days over weekdays ", maxHours//24)
	print("additional hours ", maxHours%24)
def total(hours, row, col):
	sumHours= [0]*row
	for i in range(row):
		for j in range(col):
			sumHours[i] = sumHours[i]+hours[i][j]
	return sumHours


main()	
