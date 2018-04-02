#name: Tyler
#date: sep 24
#this program will calculate the 
#perimeter and area of the rectangle
#and the area of the circle

#Part I: Input

width = float(input("please enter width of rectangle "))
length = float(input("please enter length of rectangle "))
radius = float(input("pleae enter radius of circle "))

#Part II: Calculations

area = width * length 
perimeter = 2*length + 2*width 
areaCircle = 3.14 * radius * radius 

#Part III: Results

print("Area of the rectangle is ")
print(area)
print("Perimeter of the rectangle is ")
print(perimeter)
print("Area of the circle ")
print(areaCircle)
 
