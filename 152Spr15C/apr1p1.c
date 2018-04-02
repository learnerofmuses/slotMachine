/*write the following functions:
1. void printLine(char ch, int n) - function prints
ch n times on one line 
2. void printTr(char ch, int n) - function prints
triangle of ch, triangle has n lines 
3. void printTrU(char ch, int n) - function prints 
upside down triangle 
4. void printSq(char ch, int n) - function prints 
square of ch
5. void Menu(int choice) - if choice is 1, print triangle 
if choice is 2 print upside down triangle
if choice 3 print square
and if choice is any other number print invalid message */

#include<stdio.h>
void printLine(char ch, int n);
void printTr(char ch, int n);
void printTrU(char ch, int n);
void printSq(char ch, int n);
void Menu(int choice);

int main(){
	int choice;
	printf("enter your choice, first negative stops \n");
	scanf("%d", &choice);
	while(choice>0){
		Menu(choice);
		printf("enter your choice: \n");
		scanf("%d", &choice);
	}
	return 0;
}

void printLine(char ch, int n){
	int i;
	for (i = 1; i<=n; i++){
		printf("%c", ch);
	}
}
void printTr(char ch, int n){
	int i;
	for (i = 1; i<=n; i++){
		printLine(ch, i);
		printf("\n");
	}
}
void printTrU(char ch, int n){
	int i; 
	for (i= n; i>=1; i--){
		printLine(ch, i);
		printf("\n");	
	}
}
void printSq(char ch, int n){
	int i;
	for (i = 1; i<=n; i++){
		printLine(ch, n);
		printf("\n");
	}
}
void Menu(int choice){
	char ch;
	int n;
	switch(choice){
		case 1:
			printf("printing triangle enter char and int:\n");
			ch=getchar();
			scanf("%d", &n);
			printTr(ch, n);
			break;
		case 2:
			printf("printing upside down triangle enter char and int:\n");
			ch=getchar();
			scanf("%d", &n);
			printTrU(ch, n);
			break;
		case 3:
			printf("printing sqaure enter char and int:\n");
			ch=getchar();
			scanf("%d", &n);
			printSq(ch, n);
			break;
		default:
			printf("invalid choice\n");
			break;
	}
}
