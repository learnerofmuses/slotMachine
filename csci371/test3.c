#include <GL/glut.h>
#include <GL/gl.h> 
#include <GL/glu.h> 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#define dtr 0.017453

GLfloat theta = 0.0; 

void display(){ 
	double wheel = 1.2; 
	double scale = 55;
	
	glClear(GL_COLOR_BUFFER_BIT); 
	glPointSize(35.0); 
	glLineWidth(2.5);  
	glColor3f(0,0,1); 
	

	//first wheel 
	glBegin(GL_POLYGON); 
		glVertex2f(wheel*cos(dtr*(theta + 5)), 1.0 + wheel*sin(dtr*(theta + 5))); 
		glVertex2f(wheel*cos(dtr*(theta + 175)), 1.0 + wheel*sin(dtr*(theta + 175)));
		glVertex2f(wheel*cos(dtr*(theta + 185)), 1.0 + wheel*sin(dtr*(theta + 185)));
		glVertex2f(wheel*cos(dtr*(theta + 355)), 1.0 + wheel*sin(dtr*(theta + 355)));
	glEnd(); 
	//second wheel
	glBegin(GL_POLYGON); 
		glVertex2f(wheel*cos(dtr*(theta + 85)), 1.0 + wheel*sin(dtr*(theta + 85)));
		glVertex2f(wheel*cos(dtr*(theta + 95)), 1.0 + wheel*sin(dtr*(theta + 95)));
		glVertex2f(wheel*cos(dtr*(theta + 265)), 1.0 + wheel*sin(dtr*(theta + 265)));
		glVertex2f(wheel*cos(dtr*(theta + 275)), 1.0 + wheel*sin(dtr*(theta + 275)));
	glEnd(); 
}
	//third wheel 
	 glBegin(GL_POLYGON);
                glVertex2f(wheel*cos(dtr*(theta + 5)), 1.0 + wheel*sin(dtr*(theta + 5)));
                glVertex2f(wheel*cos(dtr*(theta + 175)), 1.0 + wheel*sin(dtr*(theta + 175)));
                glVertex2f(wheel*cos(dtr*(theta + 185)), 1.0 + wheel*sin(dtr*(theta + 185)));
                glVertex2f(wheel*cos(dtr*(theta + 355)), 1.0 + wheel*sin(dtr*(theta + 355)));
        glEnd();
	//fourth wheel 
	 glBegin(GL_POLYGON);
                glVertex2f(wheel*cos(dtr*(theta + 5)), 1.0 + wheel*sin(dtr*(theta + 5)));
                glVertex2f(wheel*cos(dtr*(theta + 175)), 1.0 + wheel*sin(dtr*(theta + 175)));
                glVertex2f(wheel*cos(dtr*(theta + 185)), 1.0 + wheel*sin(dtr*(theta + 185)));
                glVertex2f(wheel*cos(dtr*(theta + 355)), 1.0 + wheel*sin(dtr*(theta + 355)));
        glEnd();

void motion(){ 
	theta =+ 0.25; 
	if(theta>360.0) theta -= 360.0; 
	glutPostRedisplay(); 
}

void keyboard(unsigned char key, int x, int y){ 
	if(key=='q' || key == 'Q')exit(0); 
	if(key=='c')glutIdleFunc(motion); 
	if(key=='s')glutIdleFunc(NULL); 
}

void reshape(GLsizei w, GLsizei h){
	GLsizei ww, hh; 
	float scale = 3.0; 
	float widthw = scale; 
	float heighth = scale; 
	
	glClearColor(0.0, 0.3,0.6, 1.0); 
#define SCALE 0.1
	glMatrixMode(GL_PROJECTION); 
	glLoadIdentity(); 
	
	if(w <= h){
		gluOrtho2D(-1*scale, scale, -1*scale*(GLfloat)h/(GLfloat)w, scale*(GLfloat)h/(GLfloat)w); 
	}
	else{ 
		gluOrtho2D(-1*scale*(GLfloat)w/(GLfloat)h, scale*(GLfloat)w/(GLfloat)h, -1*scale, scale); 
	} 
}
int main(int argc, char** argv){ 
	glutInit(&argc, argv); 	
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB); 
	glutInitWindowSize(600, 600); 
	glutInitWindowPosition(0, 0); 
	glutCreateWindow("Bike"); 
	glutReshapeFunc(reshape); 
	glutDisplayFunc(display); 
	glutKeyboardFunc(keyboard); 
	glutMainLoop(); 
}

