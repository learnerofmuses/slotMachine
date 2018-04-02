#include <GL/glut.h>

void display() {
	int i;

	glClear(GL_COLOR_BUFFER_BIT);
	glPointSize(3.0);
	glBegin( GL_POINTS );
	 glColor3f(0.0, 1.0, 0.0);
	 for(i=0; i<=10; i++){
	   glVertex2f(0.1*i, 0.1*i);
	 }
	glEnd();

	glFlush();
}

int main(int argc, char** argv){

	glutInit(&argc, argv);
	glutCreateWindow("First example");
	glutDisplayFunc( display );
	glutMainLoop();
}
