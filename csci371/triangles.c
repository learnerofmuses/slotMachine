#include <GL/glut.h>


void display(){

        glClear(GL_COLOR_BUFFER_BIT);

//      glPointSize(10.0);


        glBegin( GL_POLYGON );
         glColor3f(1.0, 1.0, 1.0);
         glVertex2f(1.5, 1.5);
         glColor3f(0.0, 1.0, 0.0); //green 
         glVertex2f(-1.5, 1.5);
         glColor3f(0.0, 0.0, 1.0); //blue
         glVertex2f(-1.5, -1.5);
         glColor3f(0., 1.0, 1.); //w 
	glVertex2f(1.5, -1.5);
        glEnd();

        glFlush(); 
}
void init() {
	glClearColor(1.0, 1.0, 1.0, 0.0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-4.0, 4.0, -4.0, 4.0);
}
int main(int argc, char** argv){
        glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(400, 400);
        glutInitWindowPosition(0,0);
        glutCreateWindow("Second Example");
	init( );
        glutDisplayFunc( display ); 
	glutMainLoop();
}
