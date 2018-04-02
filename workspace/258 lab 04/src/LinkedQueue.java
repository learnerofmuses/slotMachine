//Tyler Scott

import java.util.NoSuchElementException;
import java.util.Scanner; 

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
	
	public boolean contains(Object o){
		Node walker = head; 
		while(walker!=null){
			if(walker.element.equals(o)){
				return true;
			}
			walker=walker.link;
		}
		return false; 
	}
	
	public int countOccurrences(Object o){
		int x=0; 
		Node walker = head; 
		while(walker!=null){
			if(walker.element.equals(o)){
				x++;
			}
			walker=walker.link;
		}
		return x; 
	}
	
	@Override
	public String toString(){
		String s = "";
		Node walker = head; 
		while(walker!=null){
			s+=(String)walker.element;
			s+="";
			walker=walker.link;
		}
		return s; 
	}
	
	public LinkedQueue(LinkedQueue<? extends E> q){
		Node walker = (LinkedQueue<E>.Node)q.head;
		head = walker;
		tail = walker; 
		walker = walker.link; 
		while(walker != null){
			tail.link = walker; 
			tail = tail.link;
			walker = walker.link;
		}
	}
	
	@Override
	public boolean equals(Object o){
		if(o instanceof LinkedQueue){
			Node j1 = head;
			Node j2 = ((LinkedQueue)o).head;
			
			//name of node.link will advance the walker by one spot
			while(j1!=null && j2!=null){
				if(j1.element!= j2.element){
					return false;
				}
				j1 = j1.link;
				j2 = j2.link;
			}
		}
		else{
			return false;
		}
		return true;
	}
	
	public static void main(String[] args){
		LinkedQueue<String> eagle = new LinkedQueue<String>();
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter five names into the system");
		for(int i=0; i<5; i++){
			String name = scan.nextLine();
			eagle.add(name);
		}
		//this will make a clone of the linked queue
		LinkedQueue<String> brown = new LinkedQueue<String>(eagle);
		
		//looking to see if red is same in the linked queue
		System.out.println(brown.toString());
		
		//looking to see if eagle and red are equal to each other 
		System.out.println(eagle.equals(brown));
		
		System.out.println(eagle.contains("genus"));
		
		//this for statement will print the original linked queue as a string using the remove method
		for(int i=0; i<5; i++){
			System.out.println(eagle.remove()+"");
		}
	}
	
}
