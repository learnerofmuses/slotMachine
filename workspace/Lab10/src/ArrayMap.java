import java.util.NoSuchElementException;

import javax.swing.RowFilter.Entry;


public class ArrayMap {
	private Entry[] map;
	private int size;
	
	
	public static void main(String args) {
		ArrayMap = newMap = new ArrayMap();
		newMap.put(1, "Ryu");
		newMap.put(2, "Ry");
		newMap.put(3, "Ru");
		newMap.put(4, "R");
		newMap.put(5, "Ryu");
		newMap.put(6, "Ry");
		newMap.put(7, "Ru");
		newMap.put(8, "R");
		
		for(int k: newMap.keySet()){
			System.out.println(k);
		}
		
		for(String s: newMap.valueSet()){
			System.out.println(s);
		}
		newMap.printMap();
	}

	public ArrayMap(){
		map = new Entry[10];
		size = 0;
	}
	
	public ArrayMap(int arrayLength){
		map = new Entry[arrayLength];
		size = 0;
	}
	
	
	public void printMap(){
		for(int i=0; i<size; i++){
			System.out.println("EObject"+map[i].key+""+map[i].value);
		}
	}
	
	public void put(int key, String value){
		Entry nEntryObj = new Entry(key, value);
		int cease = 0;
		for(int i=0; i<size; i++){
			if(map[i].key==nEntryObj.key){
				map[i].value=nEntryObj.value;
				cease++;
			}
		}
		if(size==map.length){
			throw new MapFulLException();
		}
		else if(cease==0){
			map[size]=nEntryObj;
			size++;
			
		}
	}
	public int size(){
		return size;
	}
	
}
