/* Write a program that reads a sequence of characters, character '%' 
will terminate the input. finds the number of lower case letters, the number 
of upper case letters, and the number of digits. */

#include<stdio.h>

int main(){

	char l;
	int Lc=0, Uc=0, dig=0;
	printf("enter the number of characters:\n");
	l=getchar();
	while(l!='%'){
		if(l >= 'a' && l <= 'z'){
			Lc++;
		}
		else if(l >= 'A' && l <= 'Z'){
			Uc++;
		}
		else if(l >= '0' && l <= '9'){
			dig++;
		}
		l=getchar();
	}
	if(Lc==0){
		printf("there are no lowercase letters\n");
	}
	else{
		printf("there are %d lowercase letters\n", Lc);
	}
	if(Uc==0){
		printf("there are no uppercase letters\n");
	}
	else{
		printf("there are %d uppercase letters\n", Uc);
	}
	if(dig==0){
		printf("there are no digits\n", dig);
	}
	else{
		printf("there are %d digits\n");
	}
	return 0;
}
	
