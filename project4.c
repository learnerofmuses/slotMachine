// Project 4 

// Tyler Scott

#include <stdio.h>
#include <math.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include<time.h>
double pi = 3.141596;

void SquaRoot(double x, double y, double t1[]){
	double ans1 = (x*x)-(y*y);
	double ans2 = (x*y)+(x*y); 
	t1[0] = ans1;
	t1[1] = ans2;
}
void addC(double x1, double y1, double x2, double y2, double t2[]){
	double ans1 = x1+x2;
	double ans2 = y1+y2;
	
	t2[0] = ans1; 
	t2[1] = ans2;
}

double radC(double x, double y){
	double rad; 
	rad = sqrt((x*x)+(y*y));
	return rad;
}

void display(){

	glClear(GL_COLOR_BUFFER_BIT);
	glClearColor(1, 1, 1, 1);

	glPointSize(3.5);


	int i = 0; 
	double t1[2];
	t1[0] = 0.5;
	t1[1] = 0.5;
	double rad = radC(t1[0], t1[1]);	
	double sum[2];
	sum[0] = 0;  
	sum[1] = 0; 
	
	glBegin( GL_POINTS ); 
	while(rad < 2 && i < 256){
	SquaRoot(sum[0], sum[1], sum);
	rad = radC(sum[0], sum[1]);
	i++;
	}

	printf("%d\n", i);
	glColor3f(0, 1, 1);
	glVertex2f(t1[0], t1[1]);

	glEnd();
	t1[0] = 0.51;
	t1[1] = 0.47;
	sum[0] = 0; 
	sum[1] = 0; 
	rad = radC(sum[0], sum[1]);
	glBegin( GL_POINTS ); 
	while(rad < 2 && i < 256){
	SquaRoot(sum[0], sum[1], sum); 	
	addC(sum[0], sum[1], t1[0], t1[1], sum);
	rad = radC(sum[0], sum[1]);
	i++;
	}

	printf("%d\n", i);
	glColor3f(0, 1, 0); 
	glVertex2f(t1[0], t1[1]);
	
	glEnd();

	glFlush();
}
	 
void init(){
	glClearColor(.5, .5, .5, .5);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-.75, .75, -.75, .75);
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(350, 350);
	glutCreateWindow("Project Cuatro");
	init();
	glutDisplayFunc( display );
	glutMainLoop();
}













