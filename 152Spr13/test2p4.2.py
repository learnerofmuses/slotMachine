#Write a function that accepts one parameter - list of strings. The 
#function finds and returns the length of the longest string, the position 
#of the longest string and the longest string itself.

def longest_string(my_list):
	max = len(my_list[0])
	max_index = 0 
	for i in range(1, len(my_list)):
		length = len(my_list[i])
		if (max < length):
			max= length
			max_index=i
	return max, max_index, my_list[max_index]

def main():
	#testing the function
	my_list=['yana', 'guy', 'python', 'programming', 'course', 'language']
	print(longest_string(my_list)) 
main()
