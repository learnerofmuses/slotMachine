
public class TicketMachine {
	private int getCost;
	private int getCashInserted;
	
	public TicketMachine() {
		getCost = 45;
		getCashInserted = 0;
	}
	//Accessor methods//
	public int getCost(){
		return getCost;
	}
	
	public int getCashInserted(){
		return getCashInserted;
	}
	
	//Mutator method//
	public void insertCash(int cash){
		if (cash > 0){
			getCashInserted = cash;
		
		}
	}	
	public void printTicket(){
		if(getCashInserted >= getCost){
			System.out.println("Departing city: Philadelphia, Arriving city: New York.");
		
		}else{
			System.out.println("Insufficent funds, the cost of a ticket is $45.");
		}
		
	}
	
	public void getChange(){
		if(getCashInserted>getCost){
			System.out.println("Your change is:" );
			getCashInserted = getCashInserted - getCost;
		}
	}
}
