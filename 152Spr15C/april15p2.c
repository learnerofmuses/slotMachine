/*write a function int searchChar(char A[], char c)
that returns position of char c in the array A or 
-1 if character not in the array*/


#include<stdio.h>
#define SIZE 100

int searchChar(char A[], char c);
int main(){
	char A[SIZE], ch;
	int result;
	printf("enter array of chars and char to search\n");
	scanf("%s", A);
	scanf("%c", &ch);
	scanf("%c", ch);
	result = (searchChar(A, ch);
	if(result!=-1){
		printf("%c located on position %d\n", ch, result+1);
	}
	else{
		printf("%c not in the array\n", ch);
	}
	return 0; 
}

int searchChar(char A[], char c);
	int=0, position = -1, found=0;
	
	while(A[i]!='\0' && found == 0){
		if(A[i]==c){
			found=1;
			position = i;
		}
		i++;
	}
	return position;
