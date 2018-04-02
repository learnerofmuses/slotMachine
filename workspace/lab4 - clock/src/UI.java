import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

/**
 * A graphical user interface for the clock program.  
 * Displays a digital clock, which is advanced once every second.
 */
public class UI implements ActionListener {

    // STATIC SECTION

    /**
     * Call this to get the program started!
     * Creates a new UI object and gives it a new ClockDisplay object.
     * @param args not used.
     */
    public static void main(String[] args)
    {
        new UI(new ClockDisplay());
    }

    // INSTANCE SECTION
    
    private ClockDisplay clock; // The object that keeps the time
    private JLabel display;     // The digital clock display
    
    private JMenuItem set;      // Menu option to set the time
    private JMenuItem quit;     // Menu option to quit the program
    
    /**
     * Constructor - builds a digital clock display that is linked to the
     * given ClockDisplay object.
     * @param clock the ClockDisplay object.
     */
    public UI(ClockDisplay clock)
    {
        this.clock = clock;
        makeFrame();
        runClock();
    }
    
    /**
     * This method responds to events, such as mouse clicks on menu options.
     * @param e the event that occurred.
     */
    public void actionPerformed(ActionEvent e) {
        Object event = e.getSource();
        if (event.equals(set)) {            // Set the time
            try {
                clock.setTime(getInt("Enter hours: "), getInt("Enter minutes: "));
            } catch (CancelledOperationException ex) {
                return;
            }
            display.setText(clock.getTime());
        } else if (event.equals(quit)) {    // Quit the program
            System.exit(0);
        } else {
            JOptionPane.showMessageDialog(null, e.getActionCommand() + " don't work so good.");
        }
    }
    
    /**
     * This runs the clock.  It operates in a continuous loop, calling
     * the ClockDisplay object's timeTick method once every second.
     */
    private void runClock()
    {
        while(true) {
            try {
                Thread.sleep(1000);             // Sleep for 1 second (1000 milliseconds)
            } catch(Exception e) {
                JOptionPane.showMessageDialog(null, "Something went horribly wrong.");
                System.exit(0);
            }
            clock.timeTick();                   // Advance the clock
            display.setText(clock.getTime());   // Update the digital display
        }  
    }
    
    /**
     * Builds the window, of course.
     */
    private void makeFrame()
    {
        JFrame frame = new JFrame("24-hour Clock");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container contentPane = frame.getContentPane();
        contentPane.setLayout(new BorderLayout());
        
        display = new JLabel(clock.getTime(), SwingConstants.CENTER);
        display.setFont(new Font(null, Font.BOLD, 100));
        contentPane.add(display, BorderLayout.CENTER);
        
        JMenuBar menu = new JMenuBar();
        JMenu file = new JMenu("File");
        set = new JMenuItem("Set clock");
        set.addActionListener(this);
        file.add(set);
        quit = new JMenuItem("Exit");
        quit.addActionListener(this);
        file.add(quit);
        menu.add(file);
        frame.setJMenuBar(menu);
        
        frame.pack();
	  frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
    
    /**
     * Gets an integer as input from the user.
     * @param msg the prompt to display.
     * @return the integer entered by the user.
     */
    private int getInt(String msg) throws CancelledOperationException
    {
        String input = JOptionPane.showInputDialog(msg);
        if (input == null) {
            throw new CancelledOperationException();
        }
        try {
            return Integer.parseInt(input);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, input + " ain't no int, Butterscotch.");
            return getInt(msg);
        }        
    }
    
    private class CancelledOperationException extends Exception {   
    }
    
}