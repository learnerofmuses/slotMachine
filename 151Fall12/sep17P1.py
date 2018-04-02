#name: Tyler
#date: Sept 17
#This program will read one positive
#3-digit number and finds the following:
#sum of the digits, product of the digits, and average of 
#the digits

#Example:
#input: 513
#output: sum = 9
#product = 15, average = 3.000000

#Example: 
#input: 475
#sum = 16
#product = 140, average = 5.333333

#by default float numbers are printed with 6 decimal digits

#475
#475%10 = 5
#475/10 = 47
#47%10 = 7
#47/10 = 4
#4%10 = 4

#Algorithm:
#use divide by 10 and modulo 10 (modulo is % - remainder)
#to separate the digits
#after digits are separated, add them, multiply them and
#to find the average divide sum of the digits by 3

#Part I: input 

#
num = int(input("enter positive 3-digit number "))

#Part II: calculations

digitLast = num % 10 
num = num / 10 
digitMid = num % 10 
num = num / 10 
digitFirst = num % 10 

sum = digitLast + digitMid + digitFirst
product = digitLast + digitMid + digitFirst
average = float(sum)/3

#Part III: output
print("Sum of the digits is ")
print(sum)
print("Product of the digits is ") 
print(product)
print("Average of the digits is ")
print(average)
