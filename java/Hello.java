import java.util.Scanner;
public class Hello{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String name = input.nextLine();
		
		System.out.println("Hello, world!");
		System.out.println("Hello, " + name + "!");
	}
}

