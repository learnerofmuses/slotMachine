/*lab 1 monday p2 with functions*/

#include<stdio.h>

int valid(int code); /*function prototype*/

int main(){
	int num, i, validResult;
	printf("enter positive 3-digit ints\n");
	scanf("%d", &num);
	while(num>0){
		if(num<100 || num>1000){
			printf("invalid input try again\n");
		else{
			validResult=valid(num);
		}
			if(validResult==1){
				printf("%d is valid code\n",  num);
			}
			else{
				printf("not valid\n");
			}
		}
		scanf("%d", &num);
	}
	return 0;
}
/*function definition*/
int valid(int code){
	int dLast, dMiddle, dFirst, sum;
	dLast=code%10;
	code=code/10;
	dMiddle=code%10;
	code=code/10;
	dFirst=code%10;
	sum=dFirst+dMiddle+dLast;
	if((dLast==dFirst)&&(dMiddle%2==0)&&(sum%4==0)){
		return 1;
	}
	else{
		return 0;
	} 
}
