#include <GL/glut.h>

void display(){

	glClear(GL_COLOR_BUFFER_BIT);

	glLineWidth(2.5);

	glBegin(GL_LINE_LOOP);
	 glColor3f(0.0, 1.0, 0.0);
	 glVertex2f(0.75, 0.75);
	 glColor3f(1.0, 1.0, 1.0);
	 glVertex2f(0.5, 0.5);
	 glColor3f(0.1, 0.1, 0.1);
	 glVertex2f(-0.5, 0.5);
	 glColor3f(.0, .0, 1.0);
	 glVertex2f(-0.5, -0.5);
	 glColor3f(0.1, .0, .0);
	 glVertex2f(0.5, -0.5);
	 glColor3f(.1, .0, .1);
	 glVertex2f(-0.75, -0.75);
	glEnd();
	glFlush();
}

int main(argc, char** argv){
	glutInit(&argc, argv);
	glutCreateWindow("house");
	glutDisplayFunc( display);
	glutMainLoop();
}
