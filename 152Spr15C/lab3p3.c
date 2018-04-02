/*Write a C program menu.c that will print the program menu. The program 
prompts the user to enter one integer number, this number will be used 
in the program to indicate the specific menu choice. You should consider 
the following choices: input 0 - exit from the menu, 1 - program asks 
the user to enter 10 integer numbers and the program will find the 
maximum and the minimum among the inputs, 2 - program asks the user to 
enter the integer and checks if the input number even or odd, 3 - 
program prints all two-digit numbers divisible by the sum of their 
digits */


#include<stdio.h>

int max_min();
int odd_even();
int divisor();
void Menu(int choice);

int main(){
	int choice;
	printf("enter choice:\n");
	scanf("%d", &choice);
	while(choice != 0){
		Menu(choice);
		printf("enter your choice, 1, 2, or 3. 0 will terminate:\n");
		scanf("%d", &choice);
	}
	return 0;
}
void Menu(int choice){
	
	switch(choice){
		
		case 0:
			printf("program is terminated\n");
			break;
		case 1:
			max_min();
			break;
		case 2:
			even_odd();
			break;
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
	max = n;
	min = n;
	while(i<9){
		scanf("%d", &n);
			if(n>max){
				max=n;
			}
			if(n<min){
				min=n;
			}
			i++;
	}
	printf("there are %d maximum numbers\n", max);
	printf("there are %d minimum numbers\n", min);
	return 0;
}

int even_odd(){
	int n;
	printf("enter an integer:\n");
	scanf("%d", &n);
	if(n%2==0){
		printf("this integer is even\n");
	}
	else{
		printf("this integer is odd\n");
	}
}

int divisor(){
	int t, sum=0, i=10;
	
	while(i<100){
		t=i;
		sum=i%10;
		t/=10;
		sum+=t;
		if(i%sum==0){
			printf("%d divisible by sum\n", i);
		}
		i++;
	}
	return 0;
}

