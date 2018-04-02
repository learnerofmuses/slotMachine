/*Tyler Scott
March 27 2013
Write a program that reads a sequence of 10 characters and prints the 
ASCII value for each character and finds the number of characters that are 
equal '*'.*/

#include <stdio.h>

int main(){

	char letter;
	int count = 0, scount = 0;
	
	for(count = 0, count < 10, count++){
		letter = getchar();
		printf("%d", letter);	


