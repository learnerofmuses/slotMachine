#include <GL/glut.h>
#include<stdlib.h>
#include<time.h>

void display( ){
	srand( (unsigned) (time(0)) );
	int rand(), i, j;

	glClear(GL_COLOR_BUFFER_BIT);

	glPointSize(3.0);
	glColor3f(0.,0., 1.0);

	glBegin( GL_POINTS);
		for( i=1; i<= 100; i++){
			j = rand() % 10;
			glVertex2f(i, j);
		}
	glEnd();

	glFlush();
}

void init( ){
	
	glClearColor(1.0, 1.0, 1.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2d(-10.0, 10.0, -10.0, 10.0);
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(400, 400);
	glutInitWindowPosition(0, 0);
	glutCreateWindow(" ");
	init( );
}
