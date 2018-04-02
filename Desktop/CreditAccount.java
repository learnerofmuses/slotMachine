import javax.swing.JOptionPane;  // Allows dialog boxes
/**
 * A credit card account.
 */
public class CreditAccount {
	
	private String name;			// customer's name
	private AccountNumber number;	// account number
	private double balance;			// current account balance
	private double limit;			// credit limit
	
	/**
	 * Create a new account for the given customer.
	 * @param name customer's name
	 */
	public CreditAccount(String customerName) {
		if (isName(customerName)) {
			name = customerName;
		} else {
			// Display dialog box with error
			JOptionPane.showMessageDialog(null, customerName + " is not a valid name, Pumpkin Head.");
		}
		number = new AccountNumber();
		balance = 0;
		limit = 1000;
	}

	// Returns true if the given string is a valid name.
	private boolean isName(String s) {
		for(int i=0; i<s.length(); i++) { // Look through string and examine each character
			char c = s.charAt(i);
			if (!((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c == '.') || (c == '-') || (c == ' '))) {
				return false;
			}
		}
		return true;
	}
	
	// ***** ACCESSOR METHODS *****
	
	public String getName() {
		return name;
	}
	
	public AccountNumber getNumber() {
		return number;
	}
	
	public double getBalance() {
		return balance;
	}
	
	public double getLimit() {
		return limit;
	}
	
	// ***** MUTATOR METHODS *****
	
	/**
	 * Increases account balance by given amount.
	 * Displays an error if the given amount is negative.
	 * @param amount amount to add to balance
	 */
	public void raiseBalance(double amount) {
		if (amount >= 0) {
			balance += amount;
		} else {
			JOptionPane.showMessageDialog(null, "Error: amount must be nonzero.");
		}
	}
	
	/**
	 * Reduces balance by given amount.
	 * Displays an error if the given amount is negative.
	 * @param amount amount to subtract from balance
	 */
	public void lowerBalance(double amount) {
		if (amount >= 0) {
			balance -= amount;
		} else {
			JOptionPane.showMessageDialog(null, "Error: amount must be nonzero.");
		}
	}
	
	/**
	 * Sets credit limit to given amount.
	 * Displays an error if the given amount is negative.
	 * @param amount new credit limit
	 */
	public void setLimit(double amount) {
		if (amount >= 0) {
			limit = amount;
		} else {
			JOptionPane.showMessageDialog(null, "Error: amount must be nonzero.");
		}
	}
	
	// ***** OTHER METHODS *****
	
	// Returns this object formatted as a string (so it can be printed).
	public String toString() {
		return number.toString() + "\t" + name + 
				"\n\tBalance: $" + String.format("%.2f", balance) +
				"\n\tLimit:   $" + String.format("%.2f", limit);
	}
	
}
