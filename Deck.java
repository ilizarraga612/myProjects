// @ Isabelle Lizarraga
package model;

import java.util.ArrayList;
import java.util.Collections;


//Stores 52 cards and can be shuffled

public class Deck {
	private ArrayList<Card> cards;

	
	public Deck() {
        cards = new ArrayList<Card>();
        for (Suit s : Suit.values()) {
            for (Rank r : Rank.values()) {
                cards.add(new Card(r, s));
            }
        }
	}
        
    public void shuffle() {
		Collections.shuffle(cards);
		
	}

	public Card deal() {
		if (cards.isEmpty()) {
			shuffle();
		}
		return cards.isEmpty() ? null : cards.remove(0);
		// TODO Auto-generated method stub
	}

	public boolean isEmpty() {
		if (cards.isEmpty()) {
			return true;
		}
		// TODO Auto-generated method stub
		return false;
	}
}



