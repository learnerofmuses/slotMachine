/*Write a program that reads a sequence of 10 characters and prints the 
ASCII value for each character and finds the number of characters that 
are equal '*'.

*/

#include<stdio.h>

int main(){
	char v;
	int count=0, i, n;
	printf("enter 10 characters:\n");
	for(i=0; i<=9; i++){
		v=getchar();
		n=(int)(v);
		printf("%d\n", n);
		if(v=='*'){
			count++;
		}
	}
	printf("there are %d *'s\n", count);
	return 0;
}
