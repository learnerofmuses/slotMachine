#Design a program that lets the user enter the total rainfall for each of 
#12 months into a list. The program should calculate and display the total 
#rainfall for the year, the average monthly rainfall,
#and the months with the highest and lowest amounts. 

def rainfall(my_list):
	sum = 0
	total = 0 
	print("what is the total rainfall for the month?")

	for i in range(12):
		if(my_list[i] > 0):
			
			sum = sum + i
			
	
			total_rainfall = total + my_list 
			average = float(sum)/total
			print("total")
	return average
	
def main():
	print("what is the the total amount of rainfalll for the month?")

main()
