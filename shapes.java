import javax.swing.JApplet;
import java.awt.*;

public class shapes extends JApplet {

	public void paint(Graphics page) {
		page.setColor(new Color(0xFF0000));
		page.fillRect(150, 150, 50, 50);
		page.drawOval(120, 120, 60, 60);
		page.setColor(new Color(0xFF000));
		page.fillOval(60, 60, 60, 60);
	}
}
