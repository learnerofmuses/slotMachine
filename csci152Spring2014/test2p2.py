def main():
	row = int(input("enter the number of rows: "))
	col = int(input("enter the number of cols: "))

	my_list = [] 

	makeList = [[0 for i in range(col)]for j in range(row)]
	user1 = int(input("enter number of students in the group: "))
	
	makeList = make_2d_list(row, col)
	
	print("original list: ")
	ave(list, row, col)	

def make_2d_list(row, col):
	
	for i in range(row):
		for j in range(col):
			print(a[i][j])
			my_list.append(a[i][j])
	return my_list
def ave(list, row, col):
	sum = 0 
	for i in range(row):
		sum = sum+list[i][i]
		ave = sum/(row*col)
	return ave





main()
