/*write a function searchAll
that has 3 parameters:
string, char, and int array of positions of char in the string

example: 
Apple, p 
array of positions: 2, 3

programming, r
array of positions: 2, 5

apple, A
array of positions: -1

Example:
aaaaa, a
array of positions: 1, 2, 3, 4, 5 

*/


#include<stdio.h>
#define SIZE 101

void searchAll(char word[], char ch, int position[]);


int main(){
	char word[SIZE], ch; 
	int position[SIZE];
	int i=0;
	for(i=0; i<SIZE; i++){
		position[i]=-1;
	}
	printf("\n");
	printf("enter string and char to search\n"); 
	scanf("%s", word);
	scanf("%c", &ch);
	scanf("%c", &ch);
	searchAll(word, ch, position);
	if(position[0]==-1){
		printf("%c is not in the %s\n", ch, word);
	}
	else{
		printf("positions are:\n");
		while(position[i]!=-1){
			printf("%d", position[i]);
			i++;
		}
		printf("\n");
	}
	return 0;
}

void searchAll(char word[], char ch, int position[]){
	int i=0, j=0;
	while(word[i]!='\0'){
		if(word[i]==ch){
			position[j]=i+1;
			j++;
		}
		i++;
	}
}

