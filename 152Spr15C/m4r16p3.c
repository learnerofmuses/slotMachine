/* functions  

write a function that has one parameter - integer
and returns 1 if integer is even and 0 otherwise

write a program that reads 10 ints
and for each int prints even or odd */

#include<stdio.h>

int evenOdd(int num); /* function prototype */

int main(){
	int num, i, fRes;
	printf("enter 10 ints\n"); 	
	for(i=1; i<=10; i++){
		scanf("%d", &num);
		fRes=evenOdd(num);
		if(fRes==1){
			printf("%d even\n", num);
		}
		else{
			printf("%d odd\n", num);
		}
	}
	return 0;	
}

int evenOdd(int num){
	if(num%2==0){
		return 1;
	}
	else{
		return 0; 
	}
}
