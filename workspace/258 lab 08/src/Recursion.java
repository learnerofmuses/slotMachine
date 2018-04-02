
public class Recursion {
	public static void main(String[] args){ 
		int size = 10;
		int[]a = new int[size]; 
		for(int s=0; s<10; s++){
			a[s] = s; 
		}
		System.out.println(sum(a)); // test sum portion  
		
		System.out.println(getIndex(a, 9)); // test getIndex portion 
	}
	public static int sum(int[] a){
		return sum(a, 0); 
		
	}
	
	private static int sum(int[] a, int i){
		if(i==a.length){
			return 0; 
		}else{
			return a[i] + sum(a, i+1); 
		}
	}
	
	public static int getIndex(int[] a, int dex){
		return getIndex(a, dex, 0);

	}
	private static int getIndex(int[] a, int i, int dex){
		//if the element does not exist then return the vaulke of -1
		if( i== a.length){
			return -1;
		//otherwise return the index
		}else{ 
			return i; 
		}
		
	}
	
}
