/**
 * A queue is a FIFO data structure.  Elements are added to the end removed from the front.
 * 
 * @author CSCI 258
 *
 * @param <E> component type
 */
public interface Queue<E> {

	/**
	 * Adds the given element to the tail of the queue.
	 * @param element element to add
	 */
	public void add(E element);
	
	/**
	 * Removed and returns the element at the head of the queue.
	 * @return element at head of queue
	 * @throws NoSuchElementException if queue is empty
	 */
	public E remove();
	
	/**
	 * Returns the size (i.e. number of elements) of the queue.
	 * @return size of queue
	 */
	public int size();
	
}
