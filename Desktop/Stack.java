/**
 * A last-in, first-out (LIFO) collection of objects.
 *  
 * @author CSCI 258
 *
 * @param <E> component type
 */
public interface Stack<E> {
	
	/**
	 * Adds the given element to the top of stack.
	 * @param e element to push on stack.
	 * @throws IllegalStateException if stack is full
	 */
	public void push(E e);
	
	/**
	 * Removes and returns element on top of stack.
	 * @return element on top of stack
	 * @throws EmptyStackException if stack empty
	 */
	public E pop();
	
	/**
	 * Returns, but does not remove, element on top of stack.
	 * @return element on top of stack
	 * @throws EmptyStackException if stack empty
	 */
	public E peek();
	
	/**
	 * Returns true if stack is empty.
	 * @return true if stack empty
	 */
	public boolean empty();
	
}