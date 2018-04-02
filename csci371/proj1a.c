/* GL_LINE_STRIP
 * GL_LINE_LOOP
 * GL_POLYGON
 * GL_POINTS
 *
 * glutReshapeFunc();
 *
 * glVertex2fv(array);
 */


#include<GL/glut.h>
#include<GL/gl.h>
#include<GL/glu.h>
#include<math.h>
#define SCALE 0.1
#include<stdlib.h>
#include<time.h>
#include<stdio.h>
#define SCALE 0.01
void add(double n1[2], double n2[2], double arr[2]);
void mult(double n1[2], double n2[2], double arr[2]);
void orbit(double z[2], double c[2], double arr[2]);
double radius(double n1[2]);
void square(double n1[2], double arr[2]);
void display(){
	//double points[3][2]={{0.5,0.5},{0.51,0.47},{0.53,0.44}};
	double c[2];
	double z[2]={0,0};
	//double c[2]={0.5,0.5};
	double arr[2];
	double last[2];
	GLfloat p[2];

	glClear(GL_COLOR_BUFFER_BIT);
	glPointSize(5.0);
	glLineWidth(5.0);
	glColor3f(0.0,1.0,1.0);

	//arr[0] = z[0];
	//arr[1] = z[1];
	//printf("Start: c = (%f, %f)\n",arr[0],arr[1]);
	glBegin(GL_POINTS);

	for(double a=-3.0; a<=2.0; a+=SCALE){
		for(double b=0.0; b<=2.0; b+=SCALE){
			//for(int j=0; j<3; j++){
			//printf("Starting with c = (%f, 
%f)\n",points[j][0],points[j][1]);
			arr[0]=0;
			arr[1]=0;
			c[0]=a;
			c[1]=b;
			//arr[0] = points[j][0];
			//arr[1] = points[j][1];
			for(int i=0; i<256; i++){
				last[0]=arr[0];
				last[1]=arr[1];
				orbit(arr,c,arr);
				p[0]=a;
				p[1]=b;
				if(radius(arr)>2){
					//printf("\tPoint %d: %d 
iterations.  Final Point:\n",j+1,i);
					//printf("\t(%f, 
%f)\n",last[0],last[1]);
					if(i==255){
						glColor3f(1.0,1.0,1.0);
					}
					else{
						glColor3f(0.0,0.0,0.0);
					}
					glVertex2fv(p);
					break;
				}
				glColor3f(1.0,1.0,1.0);
				glVertex2fv(p);
				//printf("%d: 
(%f,%f)\n",i,arr[0],arr[1]);
			}
		}
	}
	glEnd();
	glFlush();
}

void add(double n1[2], double n2[2], double arr[2]){
	arr[0]=n1[0]+n2[0];
	arr[1]=n1[1]+n2[1];
	return;
}
void mult(double n1[2], double n2[2],double arr[2]){
	arr[0]=(n1[0]*n2[0]) + -1*(n1[1]*n2[1]);
	arr[1]=(n1[0]*n2[1]) + (n1[1]*n2[0]);
}
double radius(double n1[2]){
	double temp;
	temp = sqrt(n1[0]*n1[0] + n1[1]*n1[1]);
	return temp;
}
void orbit(double z[2], double c[2], double arr[2]){
	double t1[2];
	square(z, t1);
	add(t1, c, arr);
}
void square(double n1[2], double arr[2]){
	arr[0] = (n1[0]*n1[0]) + -1*(n1[1]*n1[1]);
	arr[1] = (n1[0]*n1[1]) + (n1[1]*n1[0]);
}
/*
void drawSquare(double x, double y, double scale){
	glBegin(GL_POLYGON);
		glColor3f(1.0,0.0,0.0);
		glVertex2f(x+scale/2.0, y+scale/2.0);
		glColor3f(0.0,1.0,0.0);
		glVertex2f(x+scale/2.0, y-scale/2.0);
		glColor3f(0.0,0.0,1.0);
		glVertex2f(x-scale/2.0, y-scale/2.0);
		glColor3f(0.0,0.0,0.0);
		glVertex2f(x-scale/2.0, y+scale/2.0);
	glEnd();
}

void drawCircle(double x, double y, double r){
	glBegin(GL_LINE_LOOP);
		for(double i=0.0; i<=2*3.14159; i+=3.14159/32.0){
			glVertex2f(x+r*cos(i),y+r*cos(i));
		}
	glEnd();
}

int getRandom(int limit){
	return rand() % limit;
}
*/
void init(){
	//Background
	glClearColor(0.5,0.5,0.5,0.5);
	//MatrixMode
	glMatrixMode(GL_PROJECTION);
	//Identity Matrix
	glLoadIdentity();
	//Ortho
	gluOrtho2D(-1.0,1.0,-1.0,1.0);
}
void reshape(GLsizei w, GLsizei h){
	GLsizei ww,hh;
	float scale = 2.0;

	glClearColor(0.5,0.5,0.5,0.5);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if(w <= h){
		
gluOrtho2D(-1*scale,scale,-1*scale*(GLfloat)h/(GLfloat)w, 
scale*(GLfloat)h/(GLfloat)w);
	}
	else{
		gluOrtho2D(-1*scale*(GLfloat)w/(GLfloat)h, 
scale*(GLfloat)w/(GLfloat)h,-1*scale,scale);

	}
/*
	if(w <= h){
		gluOrtho2D(-10.0,10,-scale*(GLfloat) h/(GLfloat) w, 
scale*(GLfloat) h/(GLfloat) w);
	}
	else{
		gluOrtho2D(-scale*(GLfloat) w/(GLfloat) h, 
scale*(GLfloat) w/(GLfloat) h,-scale,scale);

	}
*/

	glMatrixMode(GL_MODELVIEW);
	glViewport(0,0,w,h);

	ww=w;
	hh=h;
}


int main(int argc, char** argv){
	
	glutInit(&argc, argv);
	
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(0,0);
	glutInitWindowSize(500,500);
	glutCreateWindow("Project 5");
	//init();
	glutReshapeFunc(reshape);
	glutDisplayFunc(display);
	glutMainLoop();
	//display();
}
