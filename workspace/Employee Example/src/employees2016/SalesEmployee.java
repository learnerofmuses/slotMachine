package employees2016;

public class SalesEmployee {
	private double commissionRate;	// Commission rate of sales earned
	private double totalSold;		// Total amount sold since last pay
	
	public SalesEmployee(String name, String title, double pay, double rate) {
		super(name, title, pay);
		commissionRate = rate;
		totalSold = 0;
	}
	
	public double getCommissionRate() {
		return commissionRate;
	}
	
	public double getTotalSold() {
		return totalSold;
	}
	
	public void updateTotalSold(double amount) {
		totalSold += amount;
	}
	
	public void clearTotalSold() {
		totalSold = 0;
	}
	
	public void setCommissionRate(double rate) {
		commissionRate = rate;
	}
	
	@Override
	public double getMonthlyPay() {
		return super.getMonthlyPay() + commissionRate * totalSold;
	}
	
	@Override
	public String toString() {
		String s = super.toString();
		s += "\n\t" + commissionRate*100 + "%";
		return s;
	}
	
}




