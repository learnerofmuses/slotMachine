/*
 * The mysterious and magnificent heap.
 * Useful for sorting and priority queueing!
 * Order your free copy today!  (Pay only shipping and handling.)
 */
import java.util.NoSuchElementException;
public class MinHeap {

	private int[] heap;   // The heap.
	private int size;     // Index of next available array slot.
	
	/*
	 * Constructor.  Creates an empty heap.  Yipee.
	 */
	public MinHeap(int capacity)
	{
		heap = new int[capacity];
		size = 0;
	}
	
	/*
	 * Returns true if the heap is empty.
	 */
	public boolean isEmpty()
	{
	    return size == 0;
	}
	
	/**
	 * Adds a new integer to the heap.
	 * @param n integer to add
	 * @throws HeapFullException if heap is full
	 */
	public void add(int n)
	{
		if (size < heap.length) {
			
			heap[size]=n;
			int c = size; 
			int p = (c-1)/2;
			while(c != 0 && n<heap[p]){
				swap(c, p);
				c = p; 
				p = (c-1)/2;
			}
			size++;
		} else {
			throw new HeapFullException();
		}
	}
	
	/**
	 * Given the index of a parent, returns the index of the smallest child,
	 * or -1 if no such child exists.
	 * @param current index of parent
	 * @return index of smallest child or -1
	 */
	private int smallestChild(int current) {
		//int[]T;
		//int p = current;
		//int c=(p*2)+1;
		//T[size] = current;
		if(current<size){
			/*where leftSide is equal to two times the index num + 1,
			 * and rightSide is equal to two times the index num + 2
			 */
			int leftSide = 2*current+1; 
			int rightSide = 2*current+2;
			if(heap[leftSide] == 0 && heap[leftSide] == 0){
				return -1; 
			}else{
				if(leftSide > rightSide){
					return rightSide;
				}else{
					return leftSide;
				}
			}
			/*return -1;
			while(currentT[c]< && p!=0){
				return T[c];
			}*/
			
		}else{
		 
		}
		return -1;
	}
	
	/**
	 * Deletes and returns the smallest integer in the heap.
	 * @return smallest element in heap
	 * @throws NoSuchElementException if heap is empty
	 */
	public int remove(){
		
		if (size == 0) {
			throw new NoSuchElementException();
		} else {
			int smallest = heap[0]; 
			heap[0] = heap[size-1];
			size--; 
			int p = 0; 
			while(heap[p] > heap[smallestChild(p)]){
				int c = smallestChild(p);
				swap(p,c); 
				p=c; 
			}
			return smallest;
		}
			/*heap--;
		}	
			if(heap > 0){
				smallestChild(0);
			}else{
				return 0;
		}*/
	}
	
	/**
	 * Returns the heap as a string.
	 */
	public String toString()
	{
		String s = "";
		for(int i=0; i<size; i++) {
			s += i + ": " + heap[i] + "\n";
		}
		return s;
	}
	
	/**
	 * Returns the heap as an array.
	 * @return array containing same elements as heap
	 */
	public int[] toArray()
	{
	    int[] a = new int[size];
	    for(int i=0; i<size; i++) {
	        a[i] = heap[i];
	    }
	    return a;
	}
	
	/**
	 * Private swap method used by add and remove.
	 * Swaps the elements in the heap at the given indexes.
	 * @param x index of first element
	 * @param y index of second element
	 */
	private void swap(int x, int y)
	{
		int temp = heap[x];
		heap[x] = heap[y];
		heap[y] = temp;
	}
	
	/**
	 * Exception that can be thrown when heap is full.
	 */
	class HeapFullException extends RuntimeException {
		// A long number with no meaning whatsoever...but makes Java happy!
		public static final long serialVersionUID = 8320632366082135L;
	}

}
