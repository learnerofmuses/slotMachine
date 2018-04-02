#include<stdio.h> 
#include<time.h>

//in this program we learn how to create a 3-dimensional table with 
objects placed on top 

GLfloat vertices[] [3] = {{0,1,0}, 

GLfloat color[]

void poly(int air, int, earth, int fire, int water){ 
	glBegin(GL_POLYGON); 
		glVertex3fv(vertices[air]); 
		glVertex3fv(vertices[earth]);
		glVertex3fv(vertices[fire]); 
		glVertex3fv(vertices[water]); 
	glEnd(); 
}

void poly2(int xera, int yal, int zues){ 
	glBegin(GL_POLYGON); 
		glVertex3fv(vertices[xera]); 
		glVertex3fv(vertices[yal]); 
		glVertex3f(vertices[zues]); 
	glEnd(); 
}
void colorCube(void){	
	poly2(0, 1, 2);
	poly2(0, 2, 4); 
	poly2(1, 3, 4, 2); 
	poly2(0, 4, 3); 
	poly2(0, 1, 3); 
	poly2(1, 2, 5); 
	poly2(2, 3, 5); 
	poly2(3, 4, 5); 
	poly2(1, 4, 5); 
} 

static GLfloat theta[] = {0.0, 0.0, 0.0}; 
static GLint axis = 2; 



void display(void){ 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); 
	glLoadIdentity(); 
	glRotatef(theta[0], 1.0, 0.0, 0.0); //this rotates x axis 
	glRotatef(theta[1], 0.0, 1.0, 0.0); //this rotates y axis 
	glRotatef(theta[2], 0.0, 0.0, 1.0); //this rotates z axis

	//push and pop matrixs chairs, tables, and teapot

	glPushMatrix(); 
	glTranslatef(0, 0, 0);
	glScalef(5, 4, .5); 
	glColor3fv(color[3]); 
	glutSolidCube(1); 
	glPopMatrix();
 
	glPushMatrix(); 
	glTranslatef(0, 0, 0); 
	glScalef(.5, .5, 3); 
	glColor3fv(color[3]); 
	glutSolidCube(1); 
	glPopMatrix(); 


	glPushMatrix(); 
	glTranslatef(0, 0, 0.5); 
	glScalef(5.0, 4.0, .3); 
	glColor3f(0, 0, 0); 
	glutSolidCube(1);
	glPopMatrix(); 
	glPushMatrix(); 
	glTranslatef(1, 0, 3);
	glScalef(9, 9, .3);
	glColor3f(.75, .55, .55); 
	glutSolidCube(1);
	glPopMatrix(); 
	glPushMatrix(); 
	glTranslatef(2.5, -1.75, 1.25); 
	glScalef(.5, .5, .3); 
	glColor3fv(color[3]); 
	glutSolidCube(1); 
	glPopMatrix();

	glPushMatrix(); 
	glTranslatef(-2.5, -1.75, 1.25); 
	glScalef(.5,.5,.3); 
	glColor3fv(color[3]); 	
	glutSolidCube(1); 
	glPopMatrix(); 
	
	glPushMatrix();
	glTranslatef(2.5, 1.75, 1.25);
	glScalef(.5, .5, .3); 
	glColor3fv(color[3]); 
	glutSolidCube(1); 
	glPopMatrix(); 
	
	glPushMatrix(); 
	glTranslatef(-2.5, 1.75, 1.25); 
	glScalef(.5, .5, .3); 
	glColor3fv(color[3]); 
	glutSolidCube(1); 
	glPopMatrix(); 

	glPushMatrix(); 
	glTranslatef(1, 1, -1); 
	glScalef(.5, .5, 1); 
	glRotatef(270, 1, 0, 0); 
	glColor3fv(color[1]); 
	glutWireTeapot(1); 
	glPopMatrix(); 

}
void spinCube(){
	theta[axis] +=5.0; 
	if(theta[axis] > 360.0) theta[axis] -=360.0; 
	glutPostRedisplay(); 
} 

void mouse(int btn, int state, int x, int y){ 
	if (btn==GLUT_LEFT_BUTTON && state==GLUT_DOWN) axis = 0; //x 
	if (btn==GLUT_MIDDLE_BUTTON && state==GLUT_DOWN) axis = 1; //y
	if (btn==GLUT_RIGHT_BUTTON && state==GLUT_DOWN) axis = 2; //z
}

void Reshape( int w, int h ){ 
	glViewPort(0, 0, w, h); 
	glMatrixMode( GL_PROJECTION ); 
	glLoadIdentity(); 
	
	if(w <= h){
		glOrtho(-8.0, 8.0, -8.0*(GLfloat)h/(GLfloat) w, 8.0*(GLfloat)h/(GLfloat)w, -10, 10); 
	}else{
		glOrtho(-8.0*(GLfloat) w/(GLfloat) h, 8.0*(GLfloat)w/(GLfloat)h, -8.0, 8.0, -10, 10);
	}
	glMatrixMode(GL_MODELVIEW); 
}

void myKeyboard(unsigned char key, int x, int y){
	if(key=='q' || key=='Q') exit(0); 
	if(key=='c' || key=='C') glutIdleFunc(spinCube); 
	if(key=='s' || key=='S') glutIdleFunc(NULL); 
}



int main(int argc, char **argv){
	glutInit(&argc, argv); 
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); 
	glutInitWindowSize( 750, 750 ); 
	glutCreateWindow("Dinner Table"); 
	glutReshapeFunc(reshape); 
	glutDisplayFunc(display); 
	glutKeyboardFunc(myKeyboard); 
	glutMouseFunc(mouse); 
	glEnable(GL_DEPTH_TEST); 
	glutMainLoop(); 
}
