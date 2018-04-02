/*Tyler Scott*/
public class Numbers {
	private int[]Athena;
	public Numbers() {
		Athena = new int[42];
		// TODO Auto-generated constructor stub
	}
	public void fillSequence(){
		for(int i=0;i<43;i++){
			Athena[i]=i+1;
		}
	}
	public void printArray(){
		for(int i=0; i<42.;i++){
			System.out.println(Athena[i]+ " ");
		}
	}
	public static void main(String[] args){
		Numbers n = new Numbers();
		n.fillSequence();
		n.printArray();
	}
	public void fillMultiple(int n){
		for(int i=0; i<42; i++){
			Athena[i]=(i+1)*n;
		}
	}
	public void printLessThan(int x){
		for(i=0; i<x; i++){
			if(Athena[i]<x){
				System.out.println(Athena[i]+ " ");
			}
		}
	}
	public boolean equals(Object other){
		if(other instanceof Numbers){
			Numbers n=(Numbers)other;
			int[]Hera=n.Athena;
			for(int i=0; i<Athena.length; i++){
				if(Athena[i]!=Hera[i]){
					return false;
				}
			}	
		return true;		
		}
		return false;
	}
}
