/*character arrays*/

#define SIZE 5/*6*/
#include<stdio.h>
#include <string.h>

int main(){
	char word[SIZE];
	int i;
	printf("enter word:\n"); 
	/*can comment this out*/
	for(i=0; i<SIZE;/*-1*/ i++){
		scanf("%c", &word[i]); 
	}

	/*word[SIZE-1]='\0';*/
	/*up until here*/
	/*scanf("%s", word);*/ /*this because uncommented when doing choice 2*/
	printf("your word is\n");
	for(i=0; i<SIZE; i++){
		printf("%c", word[i]); 
	}
	printf("\n");
	printf("second way to print word\n");
	printf("%s\n", word);
	return 0; 
	
}
