import java.util.Random;
import java.util.Date;


public class QuickSort {
	
	private static Random rand = new Random();
	 
	public static void main(String[] args) {
		testQuickSort(10000000);
	}

	public static void testQuickSort(int size) {
		int[] a = generateRandom(size);
		printArray(a);
		long start = (new Date()).getTime();
		quickSort(a);
		long end = (new Date()).getTime();
		System.out.println("Time: "+(end-start));
		printArray(a);
		if(!isSorted(a)) {
			System.out.println("ERROR: Array not sorted.");
		}
	}
	
	public static void quickSort(int[] a) {
		quickSort(a, 0, a.length-1);
	}
	
	private static void quickSort(int[] a, int start, int end) {
		if (start < end) {
			int pivot = partition(a, start, end);
			quickSort(a, start, pivot-1);
			quickSort(a, pivot+1, end);
		}
	}
	
	public static int partition(int[] a, int start, int end) {
		int left = start+1;
		int right = end;
		int pivot = pivot(a, start, end);
		swap(a, pivot, start);
		while(left <= right) {
			for(; left <= right && a[left] <= a[start]; left++);
			for(; left <= right && a[right] > a[start]; right--);
			if (left < right) {
				swap(a, left, right);
			}
		}
		swap(a, right, start);
		return right;
	}
	
	public static int pivot(int[] a, int start, int end) {
		int mid = (start + end)/2;
		int size = end-start+1;
		int left = start;
		int right = end;
		if(size>40) {
			int s = size/8;
			left = middleOf3(a, left, left+s, left+2*s);
			mid = middleOf3(a, mid-s, mid, mid+s);
			right = middleOf3(a, right-2*s, right-s, right);
		}
		return middleOf3(a, left, mid, right);
	}

	public static int middleOf3(int[] a, int x, int y, int z) 	{
		if (x >= y && x >= z) {
			if (y >= z) {
				return y;
			} else {
				return z;
			}
		} else if (x <= y && x <= z) {
			if (y >= z) {
				return z;
			} else {
				return y;
			}
		} else {
			return x;
		}
	}
	
	public static void swap(int[] a, int i, int j) {
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
	
	public static void printArray(int[] a) {
		if (a.length <= 30) {
			for(int i=0; i<a.length; i++) {
				System.out.print(a[i]+ " ");
			}
			System.out.println();
		}
	}
	
	public static int[] generateRandom(int size) {
		int[] a = new int[size];
		for(int i=0; i<size; i++) {
			a[i] = rand.nextInt(100);
		}
		return a;
	}
	
	public static boolean isSorted(int[] a) {
		for(int i=0; i<a.length-1; i++) {
			if (a[i] > a[i+1]) {
				return false;
			}
		}
		return true;
	}
	
}
