
public class TicketMachine {
// fields/attributes
private int cost;
private int money_inserted;	
//constructor
	public TicketMachine() {
	cost = 89 ;
	money_inserted = 100;
	
	}
//accessor methods
	public int getCost(){
	return cost;	
	}
	public int getCashInserted() {
		return money_inserted;
	}
//mutator methods	
	public void insertCash(int yen){
		if(yen >= 0){
			yen = money_inserted;
		}
	}
	public void printTicket(){
		if(money_inserted >= cost){
			System.out.println("New York to California=" +cost);
		}
		else{
			System.out.println("Not enough money");
	}
	public void getChange(){
		System.out.println("Money returned, $" + money_inserted);
		money_inserted = 0;
	}
	}	
