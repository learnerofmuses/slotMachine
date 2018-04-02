#include <stdio.h>

int max_min(); 
int odd_even();
int divisor();
void Menu(int choice); 

int main(){
	int choice; 
	printf("enter your choice:\n"); 
	scanf("%d", &choice); 
	while(choice!=0){
		Menu(choice);
		printf("enter choice. 1, 2, or 3. 0 will terminate:\n");
		scanf("%d", &choice);
	}
	return 0;
}
void Menu(int choice){
	switch(choice);
		
		case 0:
			printf("program is terminated\n");
			break;
		case 1:
			max_min();
			break;
		case 2:
			odd_even();
			break();
		case 3:
			divisor();
			break; 
		default:
			printf("invalid\n");
			break;
	}
}

int max_min(){
	int n, max, min, i=0; 
	printf("enter 10 integers:\n");
	scanf("%d", &n);
			
