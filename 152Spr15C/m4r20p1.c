/*write a progrma that reads a sequence of positive ints and finds sum 
and average of even numbers between 3 and 20 
write the following functions: sum abd average
 */

#include<stdio.h>
int sum();
double average(int sum, int counter);



int main(){
	printf("sum of ints is%d\n", sum());
	return 0; 
	

}
int sum(){
	int sumNum=0, num; 
	printf("enter posotive ints\n");
	scanf("%d", &num);

	while(num > 0){
		if(num%2==0 && num>=3 && num<=20){
			sumNum+=num;
		}
	}	scanf("%d", &num);
	return sum;
}
