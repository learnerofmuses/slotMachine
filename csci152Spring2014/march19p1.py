#write a program that reads a list of dates 
#split each date to the list 
#finds the number of events in specific month 

#for example:
#input: 03/19/2014 05/19/2013 04/19/2015 03/23/2013
#we want to find the number of events in March 
#assume that user enters numeric value of the month - 3

#dates = ["03/19/2014", "05/19/2013", "04/19/2015", 03/23/2013"]

#list_dates = [["03", "19", "2014"], ...
 
def main():
	
	cont = "yes"
	dates = []
	while(cont=="yes"):
		event_date=input("enter events date ")
		dates.append(event_date)
		cont=input("enter yes to proceed to no stop ")
	print("dates are ")
	print(dates)
	list_dates = [] 
	for i in range(len(dates)):
		event = dates[i].split('/')
		list_dates.append(event)
	print("separated list of dates ")
	print(list_dates)
main()
