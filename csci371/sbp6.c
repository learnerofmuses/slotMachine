/Sami Alzahrani
#include<GL/glut.h>
#include<math.h>
#define dtr 0.017453
GLfloat theta = 0.0;
float pi= 3.1459;
void display(){
	glClear(GL_COLOR_BUFFER_BIT);
	glPointSize(10.0);
        glBegin(GL_POLYGON);                    //sky
        glColor3f(.105, .105, .4);
        glVertex2f(-3, -.3);
        glVertex2f(-3, 3);
        glVertex2f(3, 3);
        glVertex2f(3,-.3);
        glVertex2f(-3, -.3);
        glEnd();

        glBegin(GL_POLYGON);
        double x, y, s=.01;
        for(int i=0; i<=36; i++){		//moon
                glColor3f(.95-s, 0.68-s, .01-s);
                x=0.3*cos((i*pi)/18)+1.5;
                y=-0.3*sin((i*pi)/18)+1.5;
                glVertex2f(x, y);
		s=s+.02;
        }
	glEnd();

	glBegin(GL_POLYGON);
        double x2, y2;
        for(int q=0; q<=36; q++){               //top of cylo
                glColor3f(.6, 0.6, .6);
                x2=.3*cos((q*pi)/36)+.6;
                y2=.3*sin((q*pi)/36)+.4;
                glVertex2f(x2, y2);
        }
        glEnd();



	glBegin(GL_POLYGON);			//grass
	glColor3f(0.0, .4, .0);
	glVertex2f(-2, -.2);
	glVertex2f(-2, -2);
	glVertex2f(2, -2);
	glVertex2f(2, -.2);
	glVertex2f(-2, -.2);
	glEnd();
	glBegin(GL_POLYGON);			//post
	glColor3f(0.6, 0.6, 0.6);
	glVertex2f(.45, -.8);
	glVertex2f(.45, .4);
	glVertex2f(.75, .4);
	glVertex2f(.75, -.8);
	glEnd();
	glBegin(GL_POLYGON);		//shader left side
	glColor3f(.5, .5 ,.5);
	glVertex2f(.3, -.7);
	glVertex2f(.3, .4);
	glVertex2f(.45 , .4);
	glVertex2f(.45, -.8);
	glEnd();
	glBegin(GL_POLYGON);		//shader right side
	glColor3f(.7, .7, .7);
	glVertex2f(.75, -.8);
	glVertex2f(.75, .4);
	glVertex2f(.9, .4);
	glVertex2f(.9, -.7);
	glEnd();
	glColor3f(0.0, 0.0, 0.0);		//shader lines
	glBegin(GL_LINES);
	glVertex2f(.45, -.8);
	glVertex2f(.45, .4);
	glEnd();
	glBegin(GL_LINES);
	glVertex2f(.75, -.8);
	glVertex2f(.75, .4);
	glEnd();
	glColor3f(.375, 0.25, 0.199);
	glBegin(GL_POLYGON);
	glVertex2f(.1*cos(dtr*theta)+.6, .1*sin(dtr*theta)+.4);
	glVertex2f(.8*sin(dtr*theta)+.6, -.8*cos(dtr*theta)+.4);
	glVertex2f(-.1*cos(dtr*theta)+.6, .1*-sin(dtr*theta)+.4);
	glVertex2f(-.8*sin(dtr*theta)+.6, .8*cos(dtr*theta)+.4);
	glEnd();
	//glColor3f(.8, 0.8, 0.8);
        glBegin(GL_POLYGON);
/*	glColor3f(.8, 0.8, 0.8);
	glBegin(GL_POLYGON);
	glVertex2f(.1*-cos(dtr*theta)+.6, .1*-sin(dtr*theta)+.4);
	glVertex2f(-.1*-cos(dtr*theta)+.6, -.1*-sin(dtr*theta)+.4);
	glVertex2f(-.8*-sin(dtr*theta)+.6, -.8*cos(dtr*theta)+.4);
	glEnd();*/
	//glColor3f(.8, 0.8, 0.8);
	glBegin(GL_POLYGON);
	glVertex2f(.1*cos(dtr*theta+80)+.6, .1*sin(dtr*theta+80)+.4);
	glVertex2f(-.1*cos(dtr*theta+80)+.6, .1*-sin(dtr*theta+80)+.4);
	glVertex2f(-.8*sin(dtr*theta+80)+.6, .8*cos(dtr*theta+80)+.4);

	glEnd();

	//glColor3f(.8, 0.8, .8);
	glBegin(GL_POLYGON);
	glVertex2f(.1*-cos(dtr*theta+80)+.6, -.1*sin(dtr*theta+80)+.4);
	glVertex2f(-.1*-cos(dtr*theta+80)+.6, 
-.1*-sin(dtr*theta+80)+.4);
	glVertex2f(-.8*-sin(dtr*theta+80)+.6, -.8*cos(dtr*theta+80)+.4);
	glEnd();
	glColor3f(0.0, 0.0, 0.0);		//stars
        glBegin(GL_POINTS);//center
        glVertex2f(.6, .4);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(-1.2, 1.6);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(-1.8, 1.8);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(1.5, 1);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(1, 1.2);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(1.8, 1.2);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(0.0, 1.8);
        glEnd();
	glColor3f(1.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(-1.5, 1.2);
	glColor3f(1.0, 1.0, 0.0);
	glBegin(GL_POINTS);
	glVertex2f(-.4, 1);
        glEnd();



	glutSwapBuffers();
}

void mymotion(){
	theta+=1;
	if(theta>360){
		theta-=360;
	}
	glutPostRedisplay();
}

void mykeyboard(unsigned char key, int x, int y){
        if(key== 'q' || key=='Q'){
                exit(0);
        }if(key=='c'){
                glutIdleFunc(mymotion);
        }if(key=='s'){
                glutIdleFunc(NULL);
        }
}


void reshape(GLsizei w, GLsizei h){
        GLsizei ww, hh;
        glClearColor(1.0, 1.0, 1.0, 0.0);
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        if(w<=h){
                gluOrtho2D(-2, 2, -2*(GLfloat) h/(GLfloat) w, 
2*(GLfloat)h/(GLfloat)w);
        }else{
                gluOrtho2D(-2*(GLfloat) w/(GLfloat) h, 
2*(GLfloat)w/(GLfloat)h, -2, 2);
        }
        glMatrixMode(GL_MODELVIEW);
        glViewport(0, 0, w, h);
        ww=w;
        hh=h;

}

int main(int argc, char ** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(400, 400);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Sample Example lamp");
	glutReshapeFunc(reshape);
	glutDisplayFunc(display);
	//glutIdleFunc(mymotion);
	glutKeyboardFunc(mykeyboard);
	glutMainLoop();
}
