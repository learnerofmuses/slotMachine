#include <GL/glut.h>
#include <GL/glu.h>
#include <GL/gl.h>


void display(){
	int x, y;
	glClear(GL_COLOR_BUFFER_BIT);

	 glBegin( GL_POLYGON );
          glColor3f(1, 0, 0);
          glVertex2f(1.5, 1.5);
          glColor3f(0, 0, 0);
          glVertex2f(-1.5, 1.5);
          glColor3f(1, 0, 0);
          glVertex2f(-1.5, -1.5);
          glColor3f(0, 0, 0);
        glVertex2f(1.5, -1.5);

        glEnd();
	

	for(int x = -4; x<=4; x++){
		for(int y = -4; y<=4; y++){ 
			glBegin( GL_POLYGON);
	 	 	 glColor3f(1, 1, 1);
	 	 	 glVertex2f((x+1),(y + 1));
	 	 	 glVertex2f(x,(y+1));
         	 	 glVertex2f(x, y);
         	 	 glVertex2f((x+1),y);

			 glEnd();
			 y++;

		}
		x++;
	}
	
	for( int x = -3; x<=4; x++){
		for(int y = -3; y<=4; y++){
			glBegin( GL_POLYGON);
                         glColor3f(2, 2, 2);
                         glVertex2f((x+1),(y + 1));
                         glVertex2f(x,(y+1));
                         glVertex2f(x, y);
                         glVertex2f((x+1),y);

                         glEnd();
                         y++;

                }
                x++;
	}
	glFlush();
}
void init(){

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-4, 4, -4, 4);
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(600, 600); 
	glutInitWindowPosition(0,0);
	glutCreateWindow("CheckerBoard");
	init( ); 
	glutDisplayFunc( display );
	glutMainLoop(); 
}
