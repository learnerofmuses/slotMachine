def process(num_cars):
	EZ_pass = 0 
	no_EZ_pass = 0 
	trucks_buses = 0 
	
	print("enter", num_cars, "of cars")
	for i in range(num):
		lp = int(input("enter license plate number "))
		if(num >= 1 and num <= 50):
			print("there are", num, "cars with EZ pass, must pay $3.00")
		elif(num >= 51 and num <= 100):
			print("there are", num, "cars without EZ pass, must pay $4.50")
		elif(num >= 101 and num <= 150):
			print("these are trucks and buses, must pay $5.00")
		else:
			print("none of these are cars, buses, or trucks")
	return EZ_pass, no_EZ_pass, trucks_buses

def cost(num_cars, fee, day):
	print("enter the numeric value of the day ")
	
def main():
	if(day > 1 and day < 7):
		print("there is no discount")
	else:
		print("there is a 10% discount")
		print(.10*num_cars)
		
