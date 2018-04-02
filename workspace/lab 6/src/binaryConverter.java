 
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class binaryConverter {
	public static void main(String[]args){
		new binaryConverter(); 
	}
	
	private JFrame frame; 
	private JLabel Dlabel;
	private JButton button;
	private JLabel Blabel;

	public binaryConverter(){
			frame = new JFrame("Binary Converter");
			frame.setLayout(new FlowLayout());
			
			//creates convert button
			button = new JButton("Convert");
			button.addActionListener(new ButtonListener());
			frame.add(button);
			
			//creates JLabel object for "Binary"
			Blabel = new JLabel("Binary:");
			frame.add(Blabel);
			
			//creates JTextField binary object 
			JTextField btext = new JTextField(15);
			frame.add(btext);
			
			//creates JLabel object for "Decimal"
			Dlabel = new JLabel("Decimal:");
			frame.add(Dlabel);
			
			//creates JTextField decimal object
			JTextField dtext = new JTextField(15);
			frame.add(dtext);
			
			//sets frame attributes
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setSize(275, 175);
			frame.setLocationRelativeTo(null);
			frame.setVisible(true);
			
	}
	
}
