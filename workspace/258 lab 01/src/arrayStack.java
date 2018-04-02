
import java.util.Scanner;
public class arrayStack<E> implements Stack<E> {
	
	private E[] panther; 
	private int size; 
	
	public arrayStack(){ 
		
		panther = (E[]) new Object[99]; 
		size = 0; 
		
	}
	public void push(E e){
		panther[size]=e;
		size++;
	}
	public E pop(){
		E popCorn = panther[size-1];
		panther[size] = null; 
		
		size--; 
		return popCorn; 
		
	}
	public E peek(){ 
		E peekaBOO = panther[size-1]; 
		return peekaBOO; 
	}
	public boolean empty(){ 
		if(size == 0 && panther[size]== null){
			return true; // this confirms that the stack is empty
		}else{
			return false; //this confirms that the stack is not empty 
		}
	}
}