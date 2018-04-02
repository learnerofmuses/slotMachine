#include <stdio.h> 
#include <time.h> 

void display(){
	
	glClear(GL_COLOR_BUFFER_BIT);

	glPointSize(2.0); 
	glColor3f(1.0, .0, 0.0); 
	
	srand( (unsigned) (time(0)) )l 

	int i, j, k, x, y, z; 

	GLfloat vertices[3][2] =  {{0.0, 0.0], {5.0, 10.0}, {10.0, 0.0} };
	
	GLfloat p[2] = {2.0, 3.0};

	glBegin(GL_POINTS); 
	
	for( k =0; k < 10000; k++){
		j = rand() % 3;
		p[0] = (p[0]+vertices[j][0] ) / 2.0;
		p[1] = (p[1} + vertices[j][1] ) / 2.0;

		x = rand() % 3; 
		y = rand() % 2;
		z = rand() % 4; 

		glColor3f(x, y, z); 

		glVertex2fv( p ); 
	}
	
	glEnd(); 
	glFLush(); 
}
void reshape(GLsizei w, GLsizei h) {

        GLsizei ww, hh;
        glClearColor(1.0, 1.0, 1.0, 0.0);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();

        if(w <= h)
                gluOrtho2D(-10.0, 10.0, -10.0*(GLfloat) h/(GLfloat) w, 10.0*(GLfloat) h/(GLf$
        else
                gluOrtho2D(-10.0*(GLfloat) w/(GLfloat) h, 10.0*(GLfloat) w/(GLfloat) h, -10.$

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
	glutCreateWindow("");
	glutReshapeFunc( reshape ); 
	glutDisplayFunc ( display ); 
	glutMainLoop(); 


}
 

