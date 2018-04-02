#PAY ATTENTION: one dimensional
#list of strings ALL OF THE SAME LENGTH it is already two-dimensional list 
#of characters

#EXAMPLE:
#my_list = ["yana", "code", "test", "with", "math", "have"]
#this list of strings could be considered as two-dimensional list of 
#characters
#each row has 4 characters and in this example we will have 6 rows. So the 
#size
#of two-dimensional list will be 6 rows and 4 columns

#yana
#code
#test
#with 
#math
#have

#see function print_list that prints the one dimensional list of strings 
#in the two-dimensional format


#write a function column_list that  has one parameter one-dimensional list 
#of strings. Treat that list as
#two dimenstional list of chars, creates the new list by COLUMNS
# Write main to test your functions and print 
#the list by COLUMNS

#the example above will be printed as:

#yctwmh
#aoeiaa
#ndsttv
#aethhe

def print_list(string_list):
        row = len(string_list)
        col = len(string_list[0])

        for i in range(row):
                print(string_list[i])


def column_list(string_list):
	new_list=[]

	row = len(string_list)
        col = len(string_list[0])
	for j in range(col):
		new_str=""
		for i in range(row):
			new_str=new_str+string_list[i][j]
		new_list.append(new_str)
	
	return new_list

def main():
	my_list = ["yana", "code", "test", "with", "math", "have"]
	print("\nprinting list as two-dimensional list")
	print_list(my_list)
	print("printing list as two-dimensional list by COLUMNS")
	new_list=column_list(my_list)
	print_list(new_list)
main()
	
