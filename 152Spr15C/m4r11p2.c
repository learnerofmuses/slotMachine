/*write a program that reads an integer - number 
of students in class then grades for each student 
and finds average of all grades*/

#include<stdio.h>
	
int main(){

	int num_stud, grade, sum = 0, i; 
	double ave;

	printf("enter number of students in class\n");
	scanf("%d", &num_stud);
	i = 0 ;
	printf("enter %d grades\n", num_stud);
	while(i<num_stud){
		scanf("%d", &grade);
		sum+=grade;
		i++;
	
	if(num_stud>0){
		ave= (double)(sum)/num_stud;
		printf("ave is %.1f\n", ave);
	}
	else{
		printf("emtpy class\n");
	}
	}
	return 0;
}
