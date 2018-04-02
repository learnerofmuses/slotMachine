//Tyler Scott//

import java.util.*; 
public class Calculator {
	public static void main(String[] args){
		Calculator edge = new Calculator();
		edge.convert(); 
		
	}
	public void convert(){ 
		Stack<Character> edge = new Stack<Character>(); 
		Scanner input = new Scanner(System.in); 
		System.out.println("enter valid expression ");
		String iFix = input.nextLine(); 	
		String pFix = ""; 
		
		Character t; 
		for(int i = 0; i<iFix.length(); i++){ 
			t = iFix.charAt(i);
			if(Character.isDigit(t)){
				pFix += t; 
			}
			if(t == '('){
				edge.push(t);
			}
			if(t == ')'){
				while(edge.peek()!='('){
					Character z = edge.pop();
					pFix+=t; 
				}
			}
			else if(t == '+' || t == '-' || t == '/' || t == '*'){
				while(!edge.isEmpty() && edge.peek()>=priority(t)){
					Character z = edge.pop();
					pFix += z; 
				}
				edge.push(t);
			}
		}
		System.out.println(pFix);
	}
	private Character priority(Character t){ 
		switch(t){
		case'*':return 0;
		case'/':return 5;
		case'+':return 0;
		case'-':return 4; 
		case'(':return 1; 
		case')':return 8; 
		default: throw new IllegalArgumentException(t+"");
		}
	}
}
