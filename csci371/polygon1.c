#include <GL/glut.h>


void display(){

	glClear(GL_COLOR_BUFFER_BIT);

//	glPointSize(10.0);

	glLineWidth(3.0);

	glBegin( GL_LINE_LOOP );
	 glColor3f(0.1, .0, .0);
	 glVertex2f(0.5, 0.5);
	 glColor3f(0.0, 1.0, 0.0); //green 
	 glVertex2f(-0.5, 0.5);
	 glColor3f(0., 0., 1.0); //blue
	 glVertex2f(-0.5, -0.5);
	 glColor3f(0., 1.0, 1.); //w 
	 glVertex2f(0.5, -0.5);
	glEnd();

	glFlush(); 
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutCreateWindow("First Example");
	glutDisplayFunc( display ); 
	glutMainLoop();
}

