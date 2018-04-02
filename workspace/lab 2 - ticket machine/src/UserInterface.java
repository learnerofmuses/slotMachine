import java.util.Scanner;

/**
 * Simple, text-based menu interface for the ticket machine program.
 * 
 * @author Adam Fischbach
 * @version Fall 2012
 *
 */
public class UserInterface {

	public static void main(String[] args) {
		TicketMachine machine = new TicketMachine();	// Create a TicketMachine object!
		Scanner input = new Scanner(System.in);			// Create a Scanner object!
		int choice;										// This will be the choice entered by the user
		
		// Do-While loop that repeats until user selects the Done option.
		do {
			// Print the menu!
			System.out.println("CASH INSERTED: $" + machine.getCashInserted() + "\n");
			System.out.println("1) Insert money");
			System.out.println("2) Purchase ticket ($" + machine.getCost() + ")");
			System.out.println("3) Get change");
			System.out.println("4) Done");
			System.out.print("Choose an option (1-4): ");
			
			choice = input.nextInt();	// Get user's choice
			System.out.println();		// Just print a blank line (so output is not all cluttered)
			
			// Decide what to do based on user's choice!
			switch(choice) {
			case 1: int howMuch;
					System.out.print("Insert how many dollars? ");
					howMuch = input.nextInt();
					machine.insertCash(howMuch);	// Call TicketMachine's insertCash method
					break;
			case 2: machine.printTicket();			// Call TicketMachine's printTicket method
					break;
			case 3: machine.getChange();			// Call TicketMachine's getChange method
				    break;
			case 4: System.out.println("Have a nice day!");
					break;
			default: System.out.println("Yeah...so, that option doesn't do anything.\n");
			}
			System.out.println();		// Just print a blank line (so output is not all cluttered)
			
		} while(choice != 4);
	}
	
}
