//This program will  rotate our cube with mouse 

#include <GL/glut.h> 

GLfloat vertices[] [3] = { {-1.0, -1.0, -1.0}, {1.0, -1.0, -1.0}, {1.0, 
1.0, -1.0}, {-1.0, 1.0, -1.0}, {-1.0, -1.0, 1.0}, {1.0, -1.0, 1.0}, 
{1.0, 1.0, 1.0}, {-1.0, 1.0, 1.0}};

GLfloat color[] [3] = { {1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}, {0.0, 0.0, 
1.0}, {1.0, 1.0, 0.0}, {1.0, 0.0, 1.0}, {0.0, 1.0, 1.0}}; 

void polygon(int a, int b, int c, int d){
	glBegin(GL_POLYGON);
	 glVertex3fv(vertices[a]);
	 glVertex3fv(vertices[b]);
	 glVertex3fv(vertices[c]);
	 glVertex3fv(vertices[d]);
	glEnd( );
}

void colorCube( void ){
//create the polygon with different colors
 glColor3fv( color[0] ); //color is red
 polygon(0,3,2,1); //front side

 glColor3fv( color[1] ); //color is green
 polygon(2,3,7,6); //right side

 glColor3fv( color[2] );  //color is blue
 polygon(3,0,4,7); //bottom side

 glColor3fv( color[3] ); //color is RG
 polygon(1,2,6,5); //top side

 glColor3fv( color[4] ); //color is GB
 polygon(4,5,6,7); //back side

 glColor3fv( color[5] ); // color is RB
 polygon(5,4,0,1); //left side
}

static GLfloat theta[] = {0.0, 0.0, 0.0};
static GLint axis = 2; // axis y

void display ( void ){

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity( ); 
	glRotatef( theta[0], 1.0, 0.0, 0.0 ); //rotate wrt x axis
	glRotatef( theta[1], 0.0, 1.0, 0.0 ); //rotate wrt y axis
	glRotatef( theta[2], 0.0, 0.0, 1.0 ); // rotate wrt z axis

	colorCube( ); //call the function colorcube
	glFlush( );
 	glutSwapBuffers( );
}

void spinCube ( ){
 	theta[axis] += 10.0;
	if (theta[axis] > 360.0) theta[axis] -= 360.0;
	glutPostRedisplay();
}

void mouse(int btn, int state, int x, int y){ //our mouse
	if (btn==GLUT_LEFT_BUTTON && state==GLUT_DOWN) axis = 0; //x
	if (btn==GLUT_MIDDLE_BUTTON && state==GLUT_DOWN) axis = 1; //y
	if (btn==GLUT_RIGHT_BUTTON && state==GLUT_DOWN) axis = 2; //z
}

void Reshape( int w, int h ){
	glViewport(0, 0, w, h); 
	glMatrixMode( GL_PROJECTION ); 
	glLoadIdentity( ); 

	if(w <= h)
		glOrtho(-2.0, 2.0, -2.0*(GLfloat) h/ (GLfloat)w, 2.0*(GLfloat) h/ (GLfloat) w, -10.0, 10.0);
	else
		glOrtho(-2.0*(GLfloat) w/ (GLfloat) h, 2.0*(GLfloat) 
w/(GLfloat) h, -2.0, 2.0, -10.0, 10.0);

	glMatrixMode( GL_MODELVIEW ); 
}

int main(int argc, char **argv){
	glutInit(&argc, argv); 
	
	glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH ); 
	glutInitWindowSize( 750, 750 ); 
	glutCreateWindow("Rotate cube"); 
	glutReshapeFunc(Reshape);
	glutDisplayFunc(display);
	glutIdleFunc(spinCube); 
	glutMouseFunc(mouse); 
	glEnable(GL_DEPTH_TEST); 
	glutMainLoop(); 
}
