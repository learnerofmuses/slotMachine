/*Tyler Scott
April 3 2013
Write a program that reads a sequence of 10 characters and prints the 
ASCII value for each character and finds the number of characters that are 
equal '*'.*/

#include <stdio.h>


int main(){

	char letter;
	int count = 0, scount = 0, value;

	for(count = 0; count < 10; count++){
		letter = getchar();
		printf("%d\n", letter);
		if(letter == '*'){ 
			value = letter;
			scount++;
		}
	
	}
	printf("there are %d stars\n", scount);
	return 0;
	}
		
