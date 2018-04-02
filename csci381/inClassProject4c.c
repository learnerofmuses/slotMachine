/*in class project*/

#include<stdio.h>
#include<math.h>
#define PI 3.1415
int main(){

	double  t, max= 5, incr= 0.1;
	double num;
	for(t=0;t<max;t+=incr){
		num =(4.0/PI)*sin(2.0*PI*t)+(1/3)*sin(6.0*PI*t)+(1/5)*sin(10.0*PI*t);
		printf("\n %f", num); 
	}
	return 0;
	}
