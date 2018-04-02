//Spinning Square
#include <GL/glut.h>
#include <math.h>
#define dtr 0.017453
#define pi 3.1415
GLfloat theta = 0.0;

void display( ){
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_POLYGON);
	glColor3f(0,0,1);
	glVertex2f(.5*cos(dtr*theta),.5*sin(dtr*theta));
	glColor3f(1,0,0);
	glVertex2f(cos(dtr*theta+(pi/5)),sin(dtr*theta+(pi/5)));
	glColor3f(1,0,1);
	glVertex2f(.5*cos(dtr*theta+(2*pi/5)),.5*sin(dtr*theta+(2*pi/5)));
	glColor3f(0,1,1);
	glVertex2f(cos(dtr*theta+(3*pi/5)),sin(dtr*theta+(3*pi/5)));
	glColor3f(1,1,0);
	
	glVertex2f(.5*cos(dtr*theta+(4*pi/5)),.5*sin(dtr*theta+(4*pi/5)));
	glColor3f(0,1,0);
	glVertex2f(cos(dtr*theta+(5*pi/5)),sin(dtr*theta+(5*pi/5)));
	glColor3f(0,1,0);
	
	glVertex2f(.5*cos(dtr*theta+(6*pi/5)),.5*sin(dtr*theta+(6*pi/5)));
	glColor3f(0,1,0);
	glVertex2f(cos(dtr*theta+(7*pi/5)),sin(dtr*theta+(7*pi/5)));
	glColor3f(0,1,0);
	
	glVertex2f(.5*cos(dtr*theta+(8*pi/5)),.5*sin(dtr*theta+(8*pi/5)));
	glColor3f(0,1,0);
	glVertex2f(cos(dtr*theta+(9*pi/5)),sin(dtr*theta+(9*pi/5)));
	glEnd();

	glutSwapBuffers();
}

void motion(){
	theta+=.2;
	if(theta > 360) theta-=360;
	glutPostRedisplay();
}
void keyboard(unsigned char key, int x, int y){
	if(key=='q'||key=='Q')exit(0);
	if(key=='c')glutIdleFunc(motion);
	if(key=='s')glutIdleFunc(NULL);
}
void init(){
	glClearColor(1.0,1.0,1.0,0.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-2.0,2.0,-2.0,2.0);
}

int main(int argc, char** argv){

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(600,600);
	glutInitWindowPosition(0,0);
	glutCreateWindow("New Tings");
	init();
	glutDisplayFunc(display);
	//glutIdleFunc(motion);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
}
