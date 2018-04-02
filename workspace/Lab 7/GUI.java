package lab;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * This class builds the GUI window for the Inventory Program and contains the
 * main method to get the program started.
 */
public class GUI implements ActionListener {

	private static GUI window; // Link to the GUI object, once created

	/**
	 * Call this to get the whole thing started. Creates GUI and Inventory
	 * objects.
	 * 
	 * @param args
	 *            not used.
	 */
	public static void main(String[] args) {
		window = new GUI(new Inventory());
	}

	/**
	 * Prints the given string to the GUI's text area.
	 * 
	 * @param msg
	 *            the text to print.
	 */
	public static void println(Object msg) {
		if (window != null) {
			window.display(msg.toString() + "\n");
		}
	}

	private Inventory inventory; // Link to the Inventory object

	private JFrame frame; // The window itself
	private JTextArea output; // The window's text area

	private JButton stock; // Button to stock a product
	private JButton sell; // Button to sell a product
	private JButton print; // Button to print data on all products
	private JButton price; // Button to check the price of a product
	private JButton total; // Button to compute the total value of products

	private JMenuItem clearDisplay; // Menu option to clear the text area
	private JMenuItem quit; // Menu option to end the program
	private JMenuItem add; // Menu option to add a new product
	private JMenuItem remove; // Menu option to delete a product

	/**
	 * Constructor!
	 * 
	 * @param inventory
	 *            an Inventory object
	 */
	public GUI(Inventory inventory) {
		this.inventory = inventory;
		inventory.addProduct("Shoes", 20.25);
		inventory.addProduct("Socks", 5.50);
		inventory.addProduct("Pants", 89.99);
		inventory.addProduct("Shirt", 49.00);
		makeFrame();
	}

	/**
	 * Displays the given string in the text area.
	 * 
	 * @param msg
	 *            the text to display.
	 */
	public void display(String msg) {
		output.append(msg);
	}

	/**
	 * Clears all text from the text area.
	 */
	public void clear() {
		output.setText("");
	}

	/**
	 * Handles all events (button and menu item clicks).
	 * 
	 * @param e
	 *            the event that occurred.
	 */
	public void actionPerformed(ActionEvent e) {
		Object event = e.getSource();
		if (event.equals(remove)) { // Remove option clicked

			JOptionPane.showMessageDialog(frame, "This doesn't work yet!");

		} else if (event.equals(total)) { // Compute Total Value button clicked

			JOptionPane.showMessageDialog(frame, "This doesn't work yet!");

		} else if (event.equals(stock)) { // Stock button clicked

			String name = JOptionPane.showInputDialog(frame,
					"Enter product name: ");
			if (name != null) {
				int number = getInt("How many items are you adding?");
				inventory.stockProduct(name, number);
			}

		} else if (event.equals(sell)) { // Sell button clicked

			String name = JOptionPane.showInputDialog(frame,
					"Enter product name: ");
			if (name != null) {
				int number = getInt("How many items are you selling?");
				inventory.sellProduct(name, number);
			}

		} else if (event.equals(add)) { // Add option clicked

			String name = JOptionPane.showInputDialog(frame,
					"Enter new product name: ");
			if (name != null) {
				double cost = getDouble("Enter individual product price: ");
				inventory.addProduct(name, cost);
			}
			
		} else if (event.equals(print)) { // Print button clicked

			inventory.printProducts();

		} else if (event.equals(price)) { // Check Price button clicked

			String name = JOptionPane.showInputDialog(frame,
					"Enter product name: ");
			if (name != null) {
				double cost = inventory.checkPrice(name);
				if (cost == -1) {
					JOptionPane.showMessageDialog(frame, name
							+ " is not a product.");
				} else {
					JOptionPane.showMessageDialog(frame, name + ": $" + cost);
				}
			}

		} else if (event.equals(clearDisplay)) { // Clear option clicked

			clear();

		} else if (event.equals(quit)) { // Exit option clicked

			JOptionPane.showMessageDialog(frame,
					"Thank you for using this Valuable program!");
			System.exit(0);

		} else { // Unknown event occurred

			JOptionPane.showMessageDialog(frame,
					"Error: " + e.getActionCommand() + " not recognized.");

		}
	}

	/**
	 * Gets an int from the user. Will keep prompting for an int until one is
	 * entered.
	 * 
	 * @param prompt
	 *            the prompt to display.
	 * @return the int entered by the user.
	 */
	private int getInt(String prompt) {
		String input = JOptionPane.showInputDialog(frame, prompt);
		try {
			return Integer.parseInt(input);
		} catch (NumberFormatException e) {
			JOptionPane.showMessageDialog(frame, "Error: " + input
					+ " is not an integer.");
			return getInt(prompt);
		}
	}

	/**
	 * Gets a double form the user. Will keep prompting for a double until one
	 * is entered.
	 * 
	 * @param prompt
	 *            the prompt to display.
	 * @return the double entered by the user.
	 */
	private double getDouble(String prompt) {
		String input = JOptionPane.showInputDialog(frame, prompt);
		try {
			return Double.parseDouble(input);
		} catch (NumberFormatException e) {
			JOptionPane.showMessageDialog(frame, "Error: " + input
					+ " is not a number.");
			return getDouble(prompt);
		}
	}

	/**
	 * Builds the GUI window with all buttons and menu items!
	 */
	private void makeFrame() {
		frame = new JFrame("Keepin' Track o' Stuff");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container pane = frame.getContentPane();
		pane.setLayout(new BorderLayout());

		output = new JTextArea();
		pane.add(new JScrollPane(output), BorderLayout.CENTER);

		JMenuBar menuBar = new JMenuBar();
		JMenu file = new JMenu("File");
		add = new JMenuItem("Add new product");
		add.addActionListener(this);
		file.add(add);
		remove = new JMenuItem("Remove product");
		remove.addActionListener(this);
		file.add(remove);
		clearDisplay = new JMenuItem("Clear display");
		clearDisplay.addActionListener(this);
		file.add(clearDisplay);
		quit = new JMenuItem("Exit");
		quit.addActionListener(this);
		file.add(quit);
		menuBar.add(file);
		frame.setJMenuBar(menuBar);

		JPanel left = new JPanel();
		left.setLayout(new GridLayout(5, 1));
		stock = new JButton("Stock");
		stock.addActionListener(this);
		left.add(stock);
		sell = new JButton("Sell");
		sell.addActionListener(this);
		left.add(sell);
		print = new JButton("Print");
		print.addActionListener(this);
		left.add(print);
		price = new JButton("Check Price");
		price.addActionListener(this);
		left.add(price);
		total = new JButton("Compute Total Value");
		total.addActionListener(this);
		left.add(total);
		pane.add(left, BorderLayout.WEST);

		frame.pack();
		frame.setSize(600, 300);
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);
	}
}