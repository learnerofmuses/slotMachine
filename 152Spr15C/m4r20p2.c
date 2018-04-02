/*write a function that reads grades of students in the class and finds 
the average of passing grades if nobody passed the course function 
returns -1 

function has one parameter - size of the class 

write main that reads number of students in the class and uses function 
you wrote finds average of passing grades */

#include<stdio.h>

double avePass(int size);

int main(){
	int size; 
	double average;
	
	printf("enter size of the class\n");
	scanf("%d", size);
	if(size<=0){
		printf("invalid size");
	}
	else{
		average=avePass(size);
		if(average!=-1){
			printf("ave %f\n", average);
		}
		else{
			printf("all failed\n");
		}
	}
	return 0;
}

double avePass(int size){
		int grade, i, sum=0, count=0;
		double ave; 
		printf("enter %d grades\n", size);
		for(i=1; i<=size; i++){
			scanf("%d", &grade);
			if(grade>=60 &&grade<=100){
				sum+=grade;
				count++;
			}
		}
		if(count>0){
			ave=(double)(sum)/count;
		}
		else{
			ave=-1;
		}
		return ave;
}
