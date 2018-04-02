package employees2016;

public class Employee {
	private String name;	// Employee's name
	private String title;	// Employee's job title
	private double pay;		// Employee's pay rate (annual salary by default)
	
	/**
	 * Constructor - creates a new Employee object
	 * @param name employee's name
	 * @param title employee's job title
	 * @param pay employee's pay rate
	 */
	public Employee(String name, String title, double pay) {
		this.name = name;
		this.title = title;
		this.pay = pay;
	}
	
	/**
	 * Returns this employee's name
	 * @return name
	 */
	public String getName() {
		return name;
	}
	
	/**
	 * Returns this employee's job title
	 * @return job title
	 */
	public String getTitle() {
		return title;
	}
	
	/**
	 * Returns this employee's pay rate
	 * @return pay rate
	 */
	public double getPay() {
		return pay;
	}
	
	/**
	 * Returns amount this employee has earned in the current month.
	 * Assumes pay rate is annual salary.
	 * @return monthly pay owed to this employee
	 */
	public double getMonthlyPay() {
		return pay / 12.0;
	}
	
	@Override
	public String toString() {
		return name + ", " + title + "\n\t$" + String.format("%.2f", pay); 
	}
	
	@Override
	public boolean equals(Object o) {
		if (o instanceof Employee) {
			Employee e = (Employee) o;
			return this.name.equals(e.name);
		} else {
			return false;
		}
	}
	
}


