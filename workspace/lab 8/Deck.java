/**
 * An object of this class maintains an ordered collection of Card objects.
 * 
 * @author Adam Fischbach
 * @version 10.08.2009
 */
public class Deck {

    private Card[] cardDeck;    // The array of Card objects
    private int numCards;       // The number of cards in the deck
    private int x;
    /**
     * Default constructor - creates a standard deck of 52 cards, shuffled.
     */
    public Deck() {
        initDeck();
        shuffle();
    }
    
    /**
     * Adds the given card to the top of the deck, 
     * but only if the deck is not full.
     * @param c the card to add.
     */
    public void addCard(Card c) {
        if (numCards < cardDeck.length) {
            cardDeck[numCards++] = c;
        }
    }
    
    /**
     * Fills the deck with the 52 standard cards.
     * Overwrites whatever cards are currently in the deck.
     * Does not shuffle the cards.
     */
    public void initDeck() {
        numCards = 0;
        cardDeck = new Card[52];
        String[] suits = {"Hearts", "Diamonds", "Spades", "Clubs"};
        for(int s=0; s<4; s++) {
            for(int r=2; r<=14; r++) {
                addCard(new Card(r, suits[s]));
            }
        }
    }
    
    /**
     * Prints all cards in the deck to standard output.
     */
    public void printDeck() {
    	//*for(int = 0; i<cardDeck.length; i++){ **/
    	for(int i=0; i<52; i++){
    		System.out.println(cardDeck[i]);
    	}
    }
    
    /**
     * Shuffles the cards in the deck.
     */
    public void shuffle() {
        Card[] applesNoOranges=new Card[1];
        for(int i=0;i<52;i++){
        	appplesNoOranges[0]=cardDeck[i];
        	cardDeck[i]=cardDeck[x];
        	cardDeck[x]=applesNoOranges[0];
        	
        	Random gen = new Random();
        	Card temp = cardDeck[i];
        	int index = i; 
        	cardDeck[i]=cardDeck[index];
        	cardDeck[index]=temp;
        	
        	x = gen.nextInt(52);
        }
    }
    
    /**
     * Returns and removes the card at the top of the deck.
     * @return the card at the top of the deck.
     */
    public Card getCard() {
    /* if(numCards > 0){
    * 		numCards--;
    * 		Card c = cardDeck[numCards];
   	* 		cardDeck[numCards] = null;
    * 		return c;
    * }else{
    * 		return null;
   *}
   */
    	for(int i=numCards; i<52; i++){
    		cardDeck[i+1] = cardDeck[i];
    	}
    	cardDeck[51] = getCard();
    	numCards--;
    	return null;  // This is just here so the method compiles
    
    }
    
    /**
     * Returns and removes the specified number of cards at the top
     * of the deck.
     * @param howMany the number of cards to return.
     * @return an array containing the removed cards.
     */
    public Card[] getManyCards(int howMany) {
    	Card[] bicycleBrand = new Card[howMany];
    	for(int B=0; B<howMany; B++){
    		bicycleBrand[B]=getCard();
    	}
	// WRITE ME!
    	return bicycleBrand;  // This is just here so the method compiles
       
    }
 
    /**
     * Returns true if this Deck is equal to the given object.
     * Two Deck objects are equal if they have the same Card objects
     * in the same order.
     * @param obj the given object
     * @return true if this object equals the given object.
     */
    public boolean equals(Object obj) {
        if (obj instanceof Deck) {
            Deck d = (Deck) obj;
            if (numCards == d.numCards) {
                for(int i=0; i<numCards; i++) {
                    if (!cardDeck[i].equals(d.cardDeck[i])) {
                        return false;
                    }
                }
                return true;
            }
        }
        return false;
    }
   
}