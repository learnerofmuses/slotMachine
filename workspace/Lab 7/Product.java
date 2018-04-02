package lab;

/**
 * An object of this class is a type of product that includes:
 * 
 * 1) The product name
 * 2) The quantity of the product available
 * 3) The individual product price
 */
public class Product {

    private String name;    // Product name
    private int quantity;   // How many items are available
    private double price;   // Price of each item
    
    // CONSTRUCTORS
    
    /**
     * Provide the name and price.
     * @param name the name of the product.
     * @param price the price of an individual item.
     */
    public Product(String name, double price) {
        this.name = name;
        this.price = price;
        quantity = 0;
    }
    
    /**
     * Provide name, price and quantity.
     * @param name the name of the product.
     * @param price the price of an individual item.
     * @param quantity the number of products in stock.
     */
    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    
    // ACCESSOR METHODS
    
    /**
     * Returns the product's name
     * @return name
     */
    public String getName() {
        return name;
    }
    
    /**
     * Returns the number of items available.
     * @return quantity
     */
    public int getQuantity() {
        return quantity;
    }
    
    /**
     * Returns the price of an item.
     * @return price
     */
    public double getPrice() {
        return price;
    }
    
    // MUTATOR METHODS
    
    /**
     * Sets a new price for the product.
     * @param newPrice the price.
     */
    public void setPrice(double newPrice) {
        price = newPrice;
    }
    
    /**
     * Increases the quantity by the given number.
     * @param number number of items added.
     */
    public void stock(int number) {
        quantity += number;
    }
    
    /**
     * Decreases the quantity by the given number.
     * @param number number of items sold.
     */
    public void sell(int number) {
        quantity -= number;
    }
    
    /**
     * Clears the inventory.
     */
    public void clear() {
        quantity = 0;
    }
    
    // SPECIAL METHODS
    
    @Override
    public String toString() {
    	return name + "\t$" + price + "\tQty: " + quantity;
    }
    
    @Override
    /**
     * Returns true if this object is equal to the given object.
     * Two Product objects are equal if they have the same name.
     */
    public boolean equals(Object o) {
    	if (o instanceof Product) {
    		return name.equals(((Product) o).name);
    	} else {
    		return false;
    	}
    }
}
    
    