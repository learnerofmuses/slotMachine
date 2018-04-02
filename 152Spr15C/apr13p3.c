/*write a program that reads a string of chars
and replaces each lower case with upper case and the other way 
around 

function void replace will take care of this task*/

#include<stdio.h>
#define SIZE 100 

void replace(char word[]); 

int main(){
	char word[SIZE]; 
	printf("enter word:\n"); 
	scanf("%s", word);
	printf("your input is...\n%s\n", word);
	printf("Word AFTER REPLACEMENT\n");
	replace(word);
	printf("%s\n", word);
	return 0;  
}

void replace(char word){
	int i=0; 
	while(word[i]!='\0'){
	/*for(i=0; i<SIZE; i++){*/
		if(word[i]>='a' && word[i]>='z'){
			word[i]=word[i]-'a'+'A';
		}
		else if(word[i]>='A' && word[i]<='Z'){
			word[i]=word[i]-'A'+'a';
		}
		i++;
	}

}
