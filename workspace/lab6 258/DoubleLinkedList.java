package lists;

import java.util.Iterator;

/**
 * Implementation of a generic linked list with next and prev links.
 * @param <E> type of elements in the list
 */
public class DoubleLinkedList<E> implements Iterable<E> {

	/**
	 * Main method to test this class!
	 */
	public static void main(String[] args) {
		DoubleLinkedList<String> dwarves = new DoubleLinkedList<String>();
		dwarves.addFirst("Happy");
		dwarves.addFirst("Dopey");
		dwarves.addFirst("Sleepy");
		dwarves.addFirst("Sneezy");
		dwarves.addFirst("Grumpy");
		dwarves.addFirst("Doc");
		dwarves.addFirst("Bashful");
		System.out.println("Printing list using printList:");
		dwarves.printList();
		System.out.println("Printing list using for-each loop:");
		for(String s : dwarves) {
			System.out.println(s + " ");
		}
		System.out.println();
		Iterator<String> s = dwarves.iterator();
	}
	
	/**
	 * This inner class defines a node in the list.
	 */
	private class Node {
		private E element;
		private Node next;
		private Node prev;
	}
	
	private Node head;	// First element in list
	private Node tail;	// Last element in list
	private int size;	// Number of elements in list
	
	/**
	 * Constructor - creates an empty list.
	 */
	public DoubleLinkedList() {
		head = null;
		tail = null;
		size = 0;
	}
	
	/**
	 * Adds the given element to the beginning of this list.
	 * @param element element to add
	 */
	public void addFirst(E element) {//FINISHED
		Node walker=new Node();
		walker.element=element;
		return newSkywalker;
		
	}

	/**
	 * Adds the given element to the end of this list.
	 * @param element element to add
	 */
	public void addLast(E element) {//FINISHED
		Node walker = new Node();
		walker.element=element;
		if(size==0){
			head=tail=walker;
			
		}else{
			walker.prev=tail;
			tail.next=walker;
			walker.next=null;
			tail=walker;
		}
		size++;
	}
	
	/**
	 * Prints the elements in this list in reverse order.
	 */
	public void printReverse() {//FINISHED
		for(Node walker=tail; walker != null; walker=walker.prev){
			System.out.print(walker.element+ "");
		}
	}
	
	/**
	 * This inner class implements the iterator for this list.
	 * The iterator travels through the list from head to tail.
	 */
	private class HappyLittleIterator implements Iterator<E> {
		
		/**
		 * Returns the next element visited by this iterator.
		 */
		public E next() { //FINISHED
			E newSkywalker = walker.element;
			walker=walker.next;
			boolean removed = false;
			for(int i=0; i<index-1;i++){
				walker=walker.next;
			}
			Node aieL = new Node();
			aieL.element=element;
			aieL.next=walker.next;
			aieL.prev=walker;
			walker.next.prev=aieL;
			walker.next=aieL;
			size++;
		}
	}	
		/**
		 * Returns true if this iterator has not visited all of the elements.
		 */
		public boolean hasNext() {//FINISHED
			return walker != null;
		}
		
		/**
		 * Removes from the list the last element returned by next().
		 * @throws IllegalStateException if there is no valid element to remove
		 */
		public void remove() {//FINISHED
			if(new Skywalker==null){
				throw new IllegalStateException;
			}
			
			else if(newSkywalker == head && newSkywalker == tail){
				newSkywalker = null;
				head = null;
				tail = null;
			}
			
			else if(newSkywalker==head){
				head=newSkywalker.next;
				newSkywalker=null;
			}
			else if(newSkywalker==tail){
				newSkywalker=null;
				tail=newSkywalker.prev;
			}
			else{
				newSkywalker.next=newSkywalker;
				newSkywalker.prev=newSkywalker;
			}
			newSkywalker=null; 
			size--;	
		}
		
	}
	
	/**
	 * Adds the given element to the list at the given index.
	 * @param index index at which to add the element
	 * @param element element to add
	 * @throws IndexOutOfBoundsException if given index is not valid
	 */
	public void add(int index, E element) {
		if (index < 0 || index > size) {
			throw new IndexOutOfBoundsException(index+"");
		} else if (index == 0){
			addFirst(element);
		} else if (index == size) {
			addLast(element);
		} else {
			Node walker = head;
			for(int i=0; i<index-1; i++) {
				walker = walker.next;
			}
			Node n = new Node();
			n.element = element;
			n.next = walker.next;
			n.prev = walker;
			walker.next.prev = n;
			walker.next = n;
			size++;
		}
	}
	
	/**
	 * Prints the elements in this list in order.
	 */
	public void printList() {
		for(Node walker = head; walker != null; walker = walker.next) {
			System.out.print(walker.element + " ");
		}
		System.out.println();
	}
	
	/**
	 * Returns an iterator for this list.
	 */
	public Iterator<E> iterator() {
		return new HappyLittleIterator();
	}
	
}
