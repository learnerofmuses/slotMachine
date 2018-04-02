/*Tyler Scott
March 15 2013
There is a treasure chest with 1 million dollars. The chest has a 5-digit 
combination lock that opens under the following conditions: the number is 
palindrome, means it reads the same in forward and reverse directions, and 
the middle digit is divisible by 5.

For example, number 43534 will open the chest, since it is a palindrome, 
it reads the same in both directions and the middle digit is divisible by 
5.

Write a program that reads one 5-digit positive integer and checks whether 
the input number opens the chest or not. The output should be YES, if the 
chest opens, and NO otherwise. If the input is out of valid range, the 
program outputs the error message.
Examples:

    Input: 12321 Output NO
    Input: 12521 Output YES
    Input: 7878787 Output Error Input
    Input: 12523 Output NO*/

#include <stdio.h>

int main(){
	
	int num; 
	int d1, d2, d3, d4, d5;
	
	printf("enter your five digit integer\n");
	scanf("%d", &num);
	
	d1 = num % 10;
	d2 = d1/10;
	d3 = d2 % 10;
	d4 = d3/10;
	d5 = d4 % 10;
	
	if(d1 == d5 && d2 == d4 && d3%5 == 0){
		printf("You have opened the chest!\n");
	}
	else if(d1 != d5 && d2!= d4 && d3%5 != 0){
		printf("The chest remains closed.\n");
	}
	
	
}
