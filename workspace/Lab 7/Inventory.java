package lab;

/**
 * An object of this class maintains an inventory of Products.
 */

private ArrayList<String> p = newArrayList<String>();
public class Inventory {

    
    /**
     * Default constructor.
     */
    public Inventory() {
        fin
    }
        
    /**
     * Prints info on all the products in inventory.
     */
    public void printProducts() {
        
    }
    
    /**
     * Add a new product type to inventory.
     * Does nothing if inventory is full.
     * @param name name of the new product.
     * @param price the price of an individual item.
     */
    public void addProduct(String name, double price) {
        
    }
    
    /**
     * Returns the Product object with the given name.
     * @param name name of the product to find.
     * @return the Prodect object or null if product not in inventory.
     */
    private Product findProduct(String name) {
        
        return null; // This is just here so the class with compile
    }
    
    /**
     * Stock an existing product.
     * Does nothing if given product is not in inventory.
     * @param name the name of the product.
     * @param moreItems number of items to add.
     */
    public void stockProduct(String name, int moreItems) {
        Product p = findProduct(name);
        if (p != null) {
            p.stock(moreItems);
        }
    }
    
    /**
     * Sell an existing product.
     * Does nothing if given product is not in inventory.
     * @param name the name of the product.
     * @param itemSold the number of items to sell.
     */
    public void sellProduct(String name, int itemsSold) {
        Product p = findProduct(name);
        if (p != null) {
            p.sell(itemsSold);
        }
    }
    
    
    
    /**
     * Returns the price of an existing product.
     * @param name the name of the product.
     * @return the price of the product or -1 if product not in inventory.
     */
    public double checkPrice(String name) {
        Product p = findProduct(name);
        if (p != null) {
            return p.getPrice();
        } else {
            return -1;
        }
    }
    
}