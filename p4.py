#name: Tyler
#date: sep 24
#this program will read your first and last name
#and a four-digit positive integer number
#find average of first and last digits 
#print output with 2 digits after decimal point 

#Part I: Input 

firstName = input("please enter your first name ")
lastName = input("please enter your last name ")
fullName = firstName + " " + lastName 
num = int(input("please enter positive 4-digit number "))
save_num = num 

#Part II: Calculations
 
digitLast = num % 10 
num = num / 10 
digitMid = num % 10 
num = num / 10
digit_MiD = num % 10 
num = num /10 
digitFirst = num % 10
num = num / 10 

average = (digitFirst + digitLast)/float(2) 

#Part III: Results

print("my full name is ")
print(fullName)
print("enter 4-digit number ")
print(save_num)
print("average of first and last digit ")
print(average)



