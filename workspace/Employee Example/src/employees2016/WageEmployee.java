package employees2016;

public class WageEmployee extends Employee{
	private hoursWorked;
	
	public WageEmployee(String name, String title, double pay){
		super(name, title, pay);
		hoursWorked = hW; 
	}
	
	public double gethoursWorked(){
		return hW; 
	}
	
	
	
	
	
	
	@Override
	public double getMonthlyPay(){
		return super.getMonthlyPay()*hW;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
