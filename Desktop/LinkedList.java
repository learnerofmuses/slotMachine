

/**
 * A linked implementation of a flexible-size list.
 * @author CSCI 258
 *
 * @param <E> component type of elements in this list
 */
public class LinkedList<E> {

	public static void main(String[] args) {
		String[] dwarfs = {"Happy", "Dopey", "Grumpy", "Sneezy", "Sleepy", "Bashful", "Doc"};
		LinkedList<String> list = new LinkedList<String>();
		for(String d : dwarfs) {
			list.add(d);
		}
		list.print();
	}
	
	/**
	 * An object of this class is a single node in a linked list.
	 */
	private class Node {
		private E element;	// Reference to element stored in this node
		private Node link;	// Reference to next node in list (or null if no next node)
		
		/**
		 * Constructor - creates a node containing the specified element.
		 * @param element element to store in this node
		 */
		public Node(E element) {
			this.element = element;
		}
	}
	
	private Node head;	// Reference to first node in list (null if list empty)
	private Node tail;	// Reference to last node in list (null if list empty)
	private int size;	// Number of elements in this list
	
	/**
	 * Default constructor - creates an empty list.
	 */
	public LinkedList() {
		head = tail = null;
		size = 0;
	}
	
	/**
	 * Returns the number of elements in this list.
	 * @return size of list
	 */
	public int size() {
		return size;
	}
	
	/**
	 * Returns the element in this list at the specified index.
	 * @param index index of element to return
	 * @return element at specified index
	 * @throws IndexOutOfBoundsException if specified index is not valid
	 */
	public E get(int index) {
		if (index < 0 || index >= size)
			throw new IndexOutOfBoundsException(index+"");
		Node walker=head;
		for(int i=0; i<index; i++, walker=walker.link);
		return walker.element;
	}
	
	/**
	 * Adds the specified element to the end of this list.
	 * @param element element to add
	 */
	public void add(E element) {
		add(size, element);
	}
	
	/**
	 * Adds the specified element to the list at the specified index.
	 * @param index index at which element will be added
	 * @param element element to add
	 * @throws IndexOutOfBoundsException if specified index is not valid
	 */
	public void add(int index, E element) {
		if (index < 0 || index > size)
			throw new IndexOutOfBoundsException(index+"");
		Node n = new Node(element);
		if(size == 0) {
			head = tail = n;
		} else if (index == 0) {
			n.link = head;
			head = n;
		} else if (index == size) {
			tail.link = n;
			tail = n;
		} else {
			Node walker = head;
			for(int i=0; i<index-1; i++, walker=walker.link);
			n.link = walker.link;
			walker.link = n;
		}
		size++;
	}
	
	/**
	 * Removes and returns the element at the specified index.
	 * @param index index of element to remove
	 * @return removed element
	 * @throws IndexOutOfBoundsException if specified index is not valid
	 */
	public E remove(int index) {
		if (index < 0 || index >= size)
			throw new IndexOutOfBoundsException(index+"");
		E doomed = null;
		if (index == 0) {
			doomed = head.element;
			head = head.link;
			if (head == null)
				tail = null;
		} else {
			Node walker=head;
			for(int i=0; i<index-1; i++, walker=walker.link);
			doomed = walker.link.element;
			walker.link = walker.link.link;
			if (walker.link == null)
				tail = walker;
		}
		size--;
		return doomed;
	}
	
	/**
	 * Prints the elements in this list to standard output.
	 */
	public void print() {
		for(Node walker=head; walker!=null; walker=walker.link) {
			System.out.print(walker.element+" ");
		}
		System.out.println();
	}
	
}
