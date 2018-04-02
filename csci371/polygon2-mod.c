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
void reshape(GLsizei w, GLsizei h) {
	
	GLsizei ww, hh; 
	glClearColor(1.0, 1.0, 1.0, 0.0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if(w <= h)
		gluOrtho2D(-4.0, 4.0, -4.0*(GLfloat) h/(GLfloat) w, 4.0*(GLfloat) h/(GLfloat) w);
	else
		gluOrtho2D(-4.0*(GLfloat) w/(GLfloat) h, 4.0*(GLfloat) w/(GLfloat) h, -4.0, 4.0);
	
	glMatrixMode(GL_MODELVIEW);
	
	glViewport(0, 0, w, h); 

	ww = w;
	hh = h; 
}
int main(int argc, char** argv){
        glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(400, 400);
        glutInitWindowPosition(0,0);
        glutCreateWindow("Second Example");
	glutReshapeFunc( reshape ); 
        glutDisplayFunc( display ); 
	glutMainLoop();
}
