/*counter-controlled repetition*/

#include<stdio.h>

	int i =1, sum = 0; 
	double average = 0.0; 

	while(i<11){ 
		sum +=i; /*sum = sum+i; */
		i++; /*i = i+1 */

	}
	average = sum/10.0; 
	printf("the average of 1, 2,...10 is %f", average);
}
