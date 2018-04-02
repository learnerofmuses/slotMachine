//something is moving 

#include <GL/glut.h>
#define dtr 0.017453
#include <math.h>
GLfloat theta = 0.0;

void display(){
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_POLYGON);
	glColor3f(1.0, 0.0, 0.0);	
	glPointSize(3.0);
	
	
	glVertex2f(cos(dtr*theta),sin(dtr*theta) );
	glVertex2f(sin(dtr*theta),-cos(dtr*theta) );
	glVertex2f(-cos(dtr*theta),-sin(dtr*theta) ); 
	glVertex2f(-sin(dtr*theta),cos(dtr*theta) ); 	 
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
	
	if( key == 'c' ) glutIdleFunc( mymotion );
	
	if( key == 's') glutIdleFunc(NULL);	
}


void init(){
	glClearColor(1.0, 1.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-2.0,2.0,-2.0,2.0);
}
int main(int argc, char** argv){
	glutInit(&*argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(400, 400); 
	glutInitWindowPosition(0,0);
	glutCreateWindow("Move Tings");
	glutDisplayFunc( display ); 
	glutIdleFunc( mymotion );
	glutKeyboardFunc( mykeyboard );	
	glutMainLoop();	
}
