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
		num =(4.0/PI)*(sin(2.0*PI*t)+(1/3)*sin(6.0*PI*t)+(1/5)*sin(10.0*PI*t)+(1/7)*sin(14.0*PI*t)+(1/9)*sin(18.0*PI*t)+(1/11)*sin(22.0*PI*t)+(1/13)*sin(26.0*PI*t)+(1/15)*sin(30.0*PI*t));
		num= x*num;
		printf("\n %f", num); 
	}
	printf("\n");
	return 0;
	}
