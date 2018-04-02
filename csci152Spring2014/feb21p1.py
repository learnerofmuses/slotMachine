#problem 2 from lab 6 wed with one change - store all 
#input items in 2-d list

def main():
	row = int(input("enter rows: "))
	col = int(input("enter columns: "))

	a = [[0 for i in range(col)] for j in range(row)] 
	print("enter ", col*row, "integers ")
	make_2d_list(a, row, col)
	print("2d list is ")
	for i in range(row):
		print(a[i])
	paint, electric, plumb=separate(a, row, col)

	if(len(paint)>0):
		print("paint is")
		print(paint)
		remove_item_wrong(paint, min_paint)
		print("paint after removal")
		print(paint)
	else:
		print("no items in paint section ")
	
	if(len(electric)>0):
		print("electric is")
		print(electric)
	else:
		print("no electric")

	if(len(plumb)>0):
		print("plumb is")
		print(plumb)
	else:
		print("no plumbing ")
def make_2d_list(a, row, col):
	for i in range(row):
		for j in range(col):
			a[i][j]=int(input(""))
def separate(a, row, col):
	paint= []
	electric= []
	plumb= [] 

	for i in range(row):
		for j in range(col):
			if(a[i][j]>=1 and a[i][j]<=10):
				paint.append(a[i][j])
			elif(a[i][j]>=11 and a[i][j]<=50):
				electric.append(a[i][j])
			elif(a[i][j]>=51 and a[i][j]<=100):
				plumb.append(a[i][j])
	return paint, electric, plumb 

def remove_item_wrong(my_list, item):
	#wrong solution!!!!
	for i in my_list:
		if (i ==item):
			my_list.remove(i)

def remove_item_correct(my_list, item):
	#correct solution
	c = count_item(my_list, item)
	min_item_list = [item]*c
	for i in min_item_list:
		my_list.remove(i)

def count_item(my_list, item):
	c = 0 
	for i in my_list:
		if(i==item):
			c+=1
	return c		

main()
