#include<stdio.h>

int count_plus();
int sumZ(int A[]);
void printAscii(char ch); 
void makeArray(int A[]);
void printArray(int A[]);



int main(){
	srand(time(NULL));
	int choice, count = 0;
	char character;	
	printf("enter choice:\n");
	scanf("%d", &choice);
	
	switch(choice){
		
		case 1:
			count_plus();
			printf("enter character:\n");
			scanf("%c", &ch);
			break; 
		case 2:
			printAscii(char ch);
			printf("enter character:\n");
			scanf("%c", &ch);
			break; 
		default:
			srand(time(NULL));
			int count, num(SIZE)={0};
			makeArray(num);
			printArray(num);
			count=sumZ(num);		
			printf("num of zeros is %d\n," count);
			break;
	}
	return 0;
}




int count_plus(){
	char l; 
	int n, count = 0;
	printf("enter the number of characters:\n");
	l=getchar();
	while(l!='*'){
		if(n=='+'){
			count++;
		}
	}
	printf("there are %d +'s\n", count);
	return 0; 
}

/*int sumZ(){*/

void printAscii(char ch){
	char ch;
	int i=0;
	printf("enter a character:\n");
	 
	while(i<ch%10){
		printf("%c", ch);
		printf("\n");
		i++;
	}
}
void makeArray(int A[]){
	int i; 
	for(i=0; i<=SIZE; i++){
		A[i]=5+rand()%11;
	}
} 
void printArray(int A[]){
	int i; 
	value = ch%10;
	for(i=1; i<=value; i++){
		printf("c\n", ch);
	}
}


