import javax.swing.JApplet;
import java.awt.Graphics;

public class Shapes extends JApplet{

	public void paint(Graphics page){
		page.drawRect(50,50,200,200);
		page.fillOval(60,60,60,60);
		page.drawOval(102,102,60,60);
		page.fillOval(144,145,60,60);
		page.drawOval(187,186,60,60);
	}

}

