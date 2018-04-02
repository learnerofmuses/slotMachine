import java.util.Random;
public class Test {

    private static Random rand = new Random();
    
    public static void main(String[] args) {
    	testMinHeap();
    }
    
    /**
     * Test method for MinHeap
     */
    public static void testMinHeap()
    {
    	int[] a = initRandom();
        MinHeap h = new MinHeap(a.length);
        for(int i=0; i<a.length; i++) {
            h.add(a[i]);
        }
        print(a);
        System.out.println("Smallest: " + h.remove());
        int[] b = h.toArray();
        print(b);
    }
    
    /**
     * Returns an array of random length with random integers.
     * @return random array
     */
    private static int[] initRandom()
    {
        int[] a = new int[rand.nextInt(40)];
        for(int i=0; i<a.length; i++) {
            a[i] = rand.nextInt(100);
        }
        return a;
    }
    
    /**
     * Prints the given array to standard output.
     * @param a array to print
     */
    private static void print(int[] a)
    {
        for(int i=0; i<a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
    
    
    
}