/**
 * An object of this class maintains an ordered collection of Card objects.
 * 
 * @author Adam Fischbach
 * @version 10.08.2009
 */
public class Deck {

    private Card[] cardDeck;    // The array of Card objects
    private int numCards;       // The number of cards in the deck
    
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

        // WRITE ME!

    }
    
    /**
     * Shuffles the cards in the deck.
     */
    public void shuffle() {

	// WRITE ME!
        
    }
    
    /**
     * Returns and removes the card at the top of the deck.
     * @return the card at the top of the deck.
     */
    public Card getCard() {
    
	// WRITE ME!
    	return null;  // This is just here so the method compiles
    
    }
    
    /**
     * Returns and removes the specified number of cards at the top
     * of the deck.
     * @param howMany the number of cards to return.
     * @return an array containing the removed cards.
     */
    public Card[] getManyCards(int howMany) {
 
	// WRITE ME!
    	return null;  // This is just here so the method compiles
       
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