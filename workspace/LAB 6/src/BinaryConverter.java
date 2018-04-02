import java.awt.event.*;
import javax.swing.*;

public class BinaryConverter {

	public BinaryConverter() {
		JFrame Frame = new JFrame("Binary Converter");
		Frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JLabel zues = new JLabel("Binary");
		JLabel hades = new JLabel("Decimal");
		JTextField minerva= new JTextField("You clicked me!");
		JTextField desmond= new JTextField("That tickles");
		JButton jupiter = new JButton("Click the button, JUST DO IT!");
		jupiter.addActionListener(newButtonListener());
		Frame.setSize(400,200);
		Frame.setVisible(true);
		
		Frame.add(zues);
		Frame.add(hades);
		Frame.add(minerva);
		Frame.add(desmond);
		Frame.add(jupiter);
		// TODO Auto-generated constructor stub
	}
public class ButtonListener implements ActionListener{
	public void actionPeformed(Action Event e){
		
	}
}
}
