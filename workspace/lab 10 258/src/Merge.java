
public class Merge {

	
	public static void main(String[] args){
		
		int[] a = new int[4];
		int[] b = new int[6];
		a[0]=1; 
		a[1]=3;
		a[2]=5;
		a[3]=6;
		b[0]=0;
		b[2]=2;
		b[3]=4;
		b[4]=7;
		b[5]=8;
		b[6]=9;
		mergeSort(a);
	}
	int[] w = new int[a.length+b.length];
	int alpha = 0;
	int beta = 0; 
	int whiskey = 0; 
	

	public static void merge(int[]a, int[]b){
		int[] w = new int[a.length+b.length];
		int alpha = 0;
		int beta = 0; 
		while([w]<w.length && beta<b.length && alpha<a.length){
			System.out.println(w.toString());
			if(a[alpha]>b[beta]){
				w[whiskey] = b[beta++];
			}else{
				w[whiskey] = a[alpha++];
			}
			whiskey++;
		}
		if(whiskey != w.length){
			
		}
	}
	
	
	public static void merge(int[] a, int s, int mid, int end){
		int[] w = new int(end - s+1);
		int start = s;
		int mid = (s+e);
	}
	
	public static void mergeSort(int[]a){
		mergeSort(a, 0, a.length-1);
	}
	int start = 1;
	private static void mergeSort(int[] a, int s, int end){
		if(s < end){
			int mid = (start+end)/2;
			mergeSort(a, start, mid);
			mergeSort(a, mid+1, end);
			merge(a, start, mid, end);
			}
		}
	}
	
}
