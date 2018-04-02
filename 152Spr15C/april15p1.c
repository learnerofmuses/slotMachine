/*write a program that reads a string of chars and removes all chars 
that are not letters

write the ollowing functions:
1. int isalpha(char c) - function returns 1 if c is letter and 0 
otherwise 

2. void remove(char old[], char new_array[]) - all letters will be 
removed from old array and new array will only have letters - use 
function isalpha

old = 'a1b2c3'
i=1 j=1
i=2
i=3 j=2
i=4
i=5 j=3
new_array = 'abc'

*/

#include<stdio.h>
#include<string.h>
#define SIZE 100
void removeChar(char old[], char new_array[]);
int isalphaNew(char c);
int main(){
	char old[SIZE], new_array[SIZE];
	printf("enter array of chars\n");
	scanf"%s", old);
	printf("old array is %s\n", old);
	removeChar(old, new_array);
	if(strlen(new_array)>0){
		printf("new array is %s\n", new_array);
	}
	else{
		printf("all chars removed\n");
	}
	return 0;
		
}

void removeChar(char old[], char new_array[]){
	int i=0, j=0; 
	while(old[i]!= '\0'){
		if(isalphaNew(old[i])){
			new_array[j]=old[i];
			i++;
			j++;
		}
		else{
			i++;
		}
	new_array[j]
	}


}
int isalpha(char c){
	if((c>='a' && c<='z') || (c<='A' && c<='Z')){
		return 1; 
	}
	else{
		return 0;
	}

}

