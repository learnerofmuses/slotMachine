#Write a program that keeps a running total of the number of bugs 
#collected during the seven days. The loop should ask for the number of 
#bugs collected for each day,and when the loop is finished, the program
#should display the total number of bugs collected. 

def bugs(num):
	count = 0 
	total = 0 
	for i in range(num):
		num = int(input("how many bugs were collected today "))
		
		total = total + num 
		count = count + 1
		print("total bugs collected", total)
				
def main():
	bugs(7)
	
main()
