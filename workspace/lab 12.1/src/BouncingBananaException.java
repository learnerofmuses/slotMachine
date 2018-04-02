
public class BouncingBananaException{
	try{
		Thread.sleep(2000);
	}catch(Interrupted exception e){
		System.out.println("Bananas don't bounce");
		System.exit(0);
	}

