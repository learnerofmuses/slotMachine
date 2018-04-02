import java.util.NoSuchElementException;

/**
 * A linked-list implementation of the Queue interface.
 * 
 * @author CSCI 258
 *
 * @param <E> component type
 */
public class LinkedQueue<E> implements Queue<E> {
	
	// Linked list is comprised of Node objects
	private class Node {
		private E element;
		private Node link;
	}
	
	private Node head;	// Reference to first node in list
	private Node tail;	// Reference to last node in list
	private int size;	// Number of elements in list
	
	public LinkedQueue() {
		head = null;
		tail = null;
		size = 0;
	}

	/**
	 * Adds the given element to the tail of the queue.
	 * @param element element to add
	 */
	@Override
	public void add(E element) {
		Node n = new Node();
		n.element = element;
		n.link = null;
		if (head == null) {
			head = n;
		} else {
			tail.link = n;
		}
		tail = n;
		size++;
	}

	/**
	 * Removed and returns the element at the head of the queue.
	 * @return element at head of queue
	 * @throws NoSuchElementException if queue is empty
	 */
	@Override
	public E remove() {
		if (head == null) {
			throw new NoSuchElementException("empty queue");
		} else {
			E doomed = head.element;
			head = head.link;
			if (head == null) {
				tail = null;
			}
			size--;
			return doomed;
		}
	}

	/**
	 * Returns the size (i.e. number of elements) of the queue.
	 * @return size of queue
	 */
	@Override
	public int size() {
		return size;
	}
	
}
