/*write a function is_alpha that has one parameter 
char array and returns True if all chars are lowercase letters and False 
otherwise*/

#include <stdio.h>
#define SIZE 101

int is_alpha(char word[]);

int main(){
	char word[SIZE];
	int result; 
	
	printf("enter word: \n");
	scanf("%s", word);
	printf("your input string is:\n");
	printf("%s", word);
	result=is_alpha(word);
	printf("%d\n", result);
	return 0;
}

int is_alpha(char word[]){
	
	int i=0, flag=1; 
	while(word[i]!='\0' && flag==1){
		if(!(word[i]>='a' && word[i]<='z')){
			flag=0; 
		}
		i++;
	}	
	return flag; 
}
