
package lab5 

//Tyler Scott

/**
 * Partial implementation of a basic linked list.
 * @author CSCI 258
 * @version Sprintg2017
 * @param <E> component type of elements in this list
 */
public class LinkedList<E> {
	
	// Defines Node objects used to build list.
	private class Node {
		E element;	// Element stored in this node
		Node link;	// Link to next node in list (or null)
		
		public Node(E element, Node link) {
			this.element = element;
			this.link = link;
		}
	}
	
	private Node head;	// Link to first node in list (or null)
	private Node tail;	// Link to last node in list (or null)
	private int size;	// Number of elements stores in this list
	
	/**
	 * Default constructor - creates an empty list.
	 */
	public LinkedList() {
		head = tail = null;
		size = 0;
	}
	
	/**
	 * Adds the given element to the end of this list.
	 * @param element element to add
	 */
	public void add(E element) {
		Node n = new Node(element, null);
		if (tail == null) {
			
			head = tail = n;
		} else {
			tail.link = n;
			tail = n;
		}
		size++;
	}
	
	/how to reverse elements in linked list**
	 * Returns the element in this list at the given index.
	 * @param index index of element to return
	 * @return element at given index
	 * @throws IndexOutOfBoundsException if given index is invalid
	 */
	public E get(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException(index+"");
		} else {
			Node walker = head;
			for(int i=0; i<index; i++, walker=walker.link);
			return walker.element;
		}
	}
	
	/**
	 * Returns the number of elements in this list.
	 * @return size of list
	 */
	public int size() {
		return size;
	}
	
	/**
	 * Returns true if this list is empty, false otherwise.
	 * @return true is list is empty
	 */
	public boolean isEmpty() {
		return size == 0;
	}
	
	/**
	 * Prints this list to standard output.
	 */
	public void printList() {
		for(Node walker = head; walker != null; walker = walker.link) {
			System.out.print(walker.element + " ");
		}
		System.out.println();
	}
	public Object clone(){
		LinkedList<E> mesmo = new LinkedList<E>();
		/*for(int z; z<size; z++){
			 s.add(this.get(z);
		*/
			Node n = head;
			while(n != head){
				Node node = new Node(n.element, null);
				if(mesmo.size ==element 0){
					mesmo.head = node;
					mesmo.tail = node;
					mesmo.size++;
				}
				
				else{
					mesmo.tail.link = node;
					mesmo.tail = node;
					mesmo.size++;
				}
				n = n.link;
			}
			return mesmo;	
	}
	/*public void add(int index, E element){
		if(index<0 ||index>size-1){
	
			throw new Indepublic Object clone(){
		LinkedList<E> mesmo = new LinkedList<E>();
		/*for(int z; z<size; z++){
			 s.add(this.get(z);
		*/
			Node n = head;
			while(n != head){
				Node node = new Node(n.element, null);
				if(mesmo.size ==element 0){
					mesmo.head = node;
					mesmo.tail = node;
					mesmo.size++;
				}
				
				else{
					mesmo.tail.link = node;
					mesmo.tail = node;
					mesmo.size++;
				}
				n = n.link;
			}
			return mesmo;	
	}
	/*public void add(int index, E element){
		if(index<0 ||index>size-1){
	
			throw new IndexOutOfBoundsException;
			
		}else{
			Node walker = head;
			for(z=0; z<index-1;z++){
				walker = walker.link;
			}
			Node a = walker.link 
			walker.link = new NContinode(element, z);
		}
	}*/
	public void reverse(){
		Node pNode = null; 
		Node cNode = head; 
		Node next = head.link;
		
		while(cNode != null){
			cNode.link = p;
			pNode = cNode;
			cNode = next;
			if(n != null){
				next = next.link;
			}
		}
		tail = head; 
		head = pNode;
	}
	
	public static void main(String[] args){
		LinkedList<Integer> list = new LinkedList<Integer>();
		
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.printList();
		list.reverse();
		list.printList();
		LinkedList<Integer> list2 = (LinkedList) list.clone();
		list2.reverse();
		list2.printList();
	}xOutOfBoundsException;
			
		}else{
			Node walker = head;
			for(z=0; z<index-1;z++){
				walker = walker.link;
			}
			Node a = walker.link 
			walker.link = new NContinode(element, z);
		}
	}*/
	public void reverse(){
		Node pNode = null; 
		Node cNode = head; 
		Node next = head.link;
		
		while(cNode != null){
			cNode.link = pNode;
			pNode = cNode;
			cNode = next;
			if(n != null){
				next = next.link;
			}
		}
		tail = head; 
		head = pNode;
	}
	
	public static void main(String[] args){
		LinkedList<Integer> list = new LinkedList<Integer>();
		
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.printList();
		list.reverse();
		list.printList();
		LinkedList<Integer> list2 = (LinkedList) list.clone();
		list2.reverse();
		list2.printList();
	}