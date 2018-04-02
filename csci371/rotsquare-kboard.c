//something is moving 

#include <GL/glut.h>
#define dtr 0.017453

GLFloat theta = 0.0;

void display(){
	GLClear(GL_COLOR_BUFFER_BIT);
	
	glColor3f(1.0, 0.0, 0.0);	
	glPointSize(3.0);
	
	glBegin( GL_POINTS );
		glVertex2f( cos(dtr*theta(, sin(dtr*theta) );
		glVertex2f( sin(dtr*theta), -cos(dtr*theta) );
		glVertex2f( -cos(dtr*theta), -sin(dtr*theta) ); 
		glVertex2f( -sin(dtr*theta), cos(dtr*theta) ); 	 
	glEnd();

	//glFlush(); 
	glutSwapBuffers();
}
void mymotion() {
	theta += 0.1;
	if(theta > 360.0) theta -= 360.0;
	glutPostRedisplay();
}		
	
void mykeyboard(unsigned char key, int x, int y){
	if( key == 'q' || key == 'Q') exit(0);
	
}

void reshape(GLsizei w, GLsizei h){
	GLsize ww, hh;
	
	glClearColor(1.0, 1.0, 0.0);
	glMatrixMode( GL_PROJECTION);	
	glLoadIdentity();

	if(w <= h)
		gluOrtho2D(-10, 10, -10 * (GLfloat) h/(GLfloat w, 10 * (GLfloat h/(GLfloat) w);
	else
		gluOrtho2D(-10 * (GLfloat) w/(GLfloat) h, 10 * (GLfloat) w/(GLfloat) h, 10, 10);
	glMatrixMode(GL_MODELVIEW);
	glViewport(0, 0, w, h); 
	
	ww =w; 
	hh = h; 
}
int main(int argc, char** argv){
	glutInit(&*argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(400, 400); 
	glutInitWindowPosition(0,0);
	glutCreateWindow("Second Example");
	glutReshapeFunc( reshape );
	glutDisplayFunc( display ); 
	glutIdleFunc( mymotion );
	glutKeyboardFunc( mykeyboard );	
	glutMainLoop();	
