#include <GL/glut.h>

void display(){
	glClear(GL_COLOR_BUFFER_BIT); 
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(-2.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0); 
	glBegin(GL_POLYGON); //bottom 1,2,3,4
		glColor3f(.2, .5, .5); 
		glVertex3f(-1, -1, 1); 
		glVertex3f(1, -1, 1); 
		glVertex3f(1, -1, -1); 
		glVertex3f(-1, -1, -1); 
	glEnd();
	glBegin(GL_POLYGON); //back 1,5,8,4
		glColor3f(.7, .8, .2); 
		glVertex3f(-1, -1, 1);
		glVertex3f(-1, 1, 1); 
		glVertex3f(-1, 1, -1); 
		glVertex3f(-1, -1, -1); 
	glEnd(); 
	glBegin(GL_POLYGON); //right
		glColor3f(.2, .2, .6); 
		glVertex3f(1, -1, 1); 
		glVertex3f(1, -1, -1); 
		glVertex3f(1, 1, -1); 
		glVertex3f(-1, 1, 1); 
	glEnd(); 
	glBegin(GL_POLYGON); //left 1, 4, 5, 8
		glColor3f(.3, .9, .5); 
		glVertex3f(-1, -1, 1);
		glVertex3f(-1, -1, -1); 
		glVertex3f(-1, 1, -1); 
		glVertex3f(-1, 1, 1); 
	glEnd(); 
	glBegin(GL_POLYGON); //front 1, 2, 6, 5
		glColor3f(.7, 0, .5); 
		glVertex3f(-1, -1, 1); 
		glVertex3f(1, -1, 1); 
		glVertex3f(1, 1, 1); 
		glVertex3f(-1, 1, 1); 
	glEnd(); 
	glBegin(GL_POLYGON); //top 5, 6, 7, 8
		glColor3f(.7, .5, .5); 
		glVertex3f(-1, 1, 1); 
		glVertex3f(1, 1, 1); 
		glVertex3f(1, 1, -1); 
		glVertex3f(-1, 1, -1); 
	glEnd(); 
	glutSwapBuffers(); 
	
}
void reshape(int w, int h){
	glViewport(0, 0, w, h); 
	glMatrixMode(GL_PROJECTION); 
	glLoadIdentity(); 
	glOrtho(-2, 2, -2, 2, -4, 4); 
}
void init(){
	glClearColor(1.0, 1.0, 1.0, 0.0); 
}

int main(int argc, char** argv){
	glutInit(&argc, argv); 
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB); 
	glutInitWindowSize(600, 600); 
	glutInitWindowPosition(0, 0); 
	glutCreateWindow("3D two objects"); 
	glutReshapeFunc(reshape); 
	init(); 
	glutDisplayFunc(display); 
	glutMainLoop(); 
}
