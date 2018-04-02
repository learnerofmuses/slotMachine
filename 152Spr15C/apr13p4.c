/*write a program that randomly generates a string of chars
length between 1 and 20 - make_string function will take care of this 
task 

check if  the string is a valid password
Conditions: 
1. length between 8 and 12 
2. has at least one digit 
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#define SIZE 21 
#define TRUE 1 
#define FALSE 0 

void make_string(char word[]); 
int valid_psswd(char word[]);

int main(){
	char word[SIZE];
	int result;
	
	srand(time(NULL));
	make_string(word);
	printf("%s\n", word);
	printf("length of string is %d\n", strlen(word));
	if(valid_psswd(word)==TRUE){
		printf("password valid!\n");
	}
	else{	
		printf("password not valid!!!\n");
	}
	return 0; 
}

void make_string(char word[]){
	int len = 1+rand%20; /*length 1 to 20*/
	int i; 
	for(i=0; i<len; i++){
		word[i]=(char)(33+rand()%94);	
		
	}
	word[len]='\0';
}

int valid_psswd(char word[]){
	int i=0, count=0, digit=0;
	/*first part - find length of the string WITHOUT using strlen*/

	while(word[i]!='\0'){
		count++; 
		i++;
	}
	i=0
	while(word[i]!='\0'){
		if(word[i]>='0' && word[i]<='9'){
			digit =1; 
		}
		i++;
	}
	if(count>=8 && count<=12 && digit == 1){
		return TRUE;
	}
	else{
		return FALSE;
	}
	
}
