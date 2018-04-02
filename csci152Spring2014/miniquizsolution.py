#Write a function def process(my_string), that has one parameter - 
#string of characters. The function counts the number of upper case 
#letters, lower case letters, and the digits. The counters will be 
#stored in one dimensional list of integers. Function returns the one 
#dimensional list of counters. Write a program that inputs one string, 
#then calls function process to find the counters, and then finds which 
#category has the most characters (Try to do this WITHOUT IF statement). 

def main():
	my_str=input("enter strings: ")
	count = process(my_str)
	print("counters ")
	print(count)

	max_value = max(count)
	max_index = count.index(max_value)

	name = ["upper", "lower", "digit"]
	max_name = name[max_index]
	

	print("max category is ", max_name)

def process(my_string):
	counters=[0]*3
	for i in my_string:
		if(i.isupper()):
			counter[0]+=1
		elif(i.islower()):
			counters[1]+=1
		elif(i.isdigit()):
			counters[2]+=1

	return counters


main()
