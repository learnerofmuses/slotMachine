import java.util.Scanner;
public class Scanner{
	public static void main(String[] args) {
	
		Scanner input = new Scanner (System.in);
		String name = input.nextLine();
		int x = input.nextInt();
	System.out.println("Hello," + name + "!");
	}
}
