

#include <GL/glut.h>


void display(){

        glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_MODELVIEW); 
	glLoadIdentity(); 
	gluLookAt(0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        glBegin( GL_POLYGON );
	glColor3f(0.0, 1.0, 1.0); 
         glVertex3f(0.5, 0.5, 1.0); 
         glVertex3f(-0.5, 0.5, 1.0);
         glVertex3f(-0.5, -0.5, 1.0); 
	 glVertex3f(0.5, -0.5, 1.0);
        glEnd();

        glutSwapBuffers(); 
}
void reshape(int w, int h){
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION); 
	glLoadIdentity(); 
	glOrtho(-2.0, 2.0, -2.0, 2.0, -4.0, 4.0); 

}
void init() {
	glClearColor(1.0, 1.0, 1.0, 0.0);

}
int main(int argc, char** argv){
        glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(400, 400);
        glutInitWindowPosition(0,0);
        glutCreateWindow("Cube");
	glutReshapeFunc(reshape);
	init( );
        glutDisplayFunc( display ); 
	glutMainLoop();
}
