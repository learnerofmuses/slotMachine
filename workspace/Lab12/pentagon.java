import java.awt.*;

/**
 * A pentagon that can be manipulated and that draws itself on a canvas.
 */
public class pentagon extends Triangle{
	
	private int height;
	private int width; 
	
	/**
     * Create a new pentagon at default position with default color.
     */
	public pentagon(){
		super(); 
		height = 75;
		width = 55;
	}
	
	 /**
     * Change the shape's size.
     */
	
	public void changeSize(int h int w){
		height = h;
		width = w; 
		draw();
	}

	
	public void draw(){
		if(isVisible()) {
		      Canvas canvas = Canvas.getCanvas();
		      int[] xPoints = {getxPosition(), getxPosition()+width/2,                
		                       getxPosition()+width/4, 
		                       getxPosition()-width/4, 
		                       getxPosition()-width/2};
		      int[] yPoints = {getyPosition(), getyPosition()-height/2, 
		                       getyPosition()-height,
		                       getyPosition()-height, 
		                       getyPosition()-height/2};
		      canvas.draw(this, getColor(), new Polygon(xPoints, yPoints, 5));
		      canvas.wait(10);
		  }
		}
}
