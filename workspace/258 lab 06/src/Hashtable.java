import java.util.LinkedList;

public class Hashtable<E> implements HTable<E> {

	LinkedList<E>[] wow;
	private int size; 
	
	@Override
	public void add(E element){
		
	}
	
	@Override
	public boolean contains(Object o){
		for(int i = 0; i<a.length; i++){
			if()
		}
		
	}
	
	public void print();
		
	
	
}


public static void main(String[] args){
	HashTable<String> h = new HashTable<String>(); 
	String s = "happy meals are quite tasty and make round children"; 
	String[] a = s.split("");
	for(String w: a){ 
		h.add(w); 
		
	}
	System.out.println(h.contains("tasty"));
	System.out.println(h.contains("fruity"));
	h.print(); 
	
}
