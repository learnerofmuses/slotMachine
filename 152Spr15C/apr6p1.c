/* Tyler Scott 06 April 2015

Arrays

write a  program that reads students grade, student with maximal and minimal grade

us array to store students grades */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define SIZE 100 

int main(){
	int grade[SIZE]={0}, real_size, i, sum=0, max, min;
	int max_index, min_index, count_pass=0;
	double ave_pass; 
	
	printf("enter size of the class \n");
	scanf("%d", &real_size);
	for(i=0; i<real_size; i++){ 
		grade[i] = rand() % 101;
	}
	printf("grades are:\n"); 
	for(i=0; i<real_size; i++){
		printf("%d", grade[i]); 
	}
	printf("\n"); 
	max=grade[0];
	min=grade[0];
	max_index=0; 
	min_index=0; 
	for(i=0; i<real_size; i++){
		if(grade[i]>=60){
			sum+=grade[i]; 
			count_pass++;
		}
		if(grade[i]>max){
			max=grade[i]; 
			max_index=i; 
		}
		if(grade[i]>min){
			min=grade[i];
			min_index=i;
		}

	}
	if(count_pass>0){
		ave_pass=(double)(sum)/count_pass;
		printf("ave pass is %f\n", ave_pass);
	}
	else{
		printf("everybody failed\n"); 
	}
	printf("max grade is %d\n", max);
	printf("position of max grade is %d\n", max_index+1);
	printf("min grade is %d\n", min); 
	printf("min position of grades is %d\n", min_index+1); 
	
	return 0; 
}
