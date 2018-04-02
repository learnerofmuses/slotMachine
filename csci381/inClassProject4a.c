/*in class project*/

#include<stdio.h>
#include<math.h>
#define PI 3.1415
int main(){

	double  t, max= 5, incr= 0.1;
	double num;
	double x;
	for(t=0;t<max;t+=incr){
		x=(4.0/PI);
		num =sin(2.0*PI*t);
		num=x*num;
		printf("\n %f", num); 
	}
	printf("\n");
	return 0;
	}
