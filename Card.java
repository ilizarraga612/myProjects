// @ Isabelle Lizarraga
package model;

public class Card implements Comparable<Card> {

	// A Card object has a known rank DEUCE (2) through ACE (14) and a known suit:
	//CLUBS ♣, DIAMONDS ♦, HEARTS ♥, and SPADES ♠ where each suit has these 13 Ranks:
	//	DEUCE  THREE  FOUR  FIVE  SIX  SEVEN  EIGHT  NINE  TEN  JACK  QUEEN  KING 
	//	ACE.  Later on. a PokerHand will store five Card objects.
	
	public Card(Rank rank, Suit suit) {
		this.rank = rank;
		this.suit = suit;
		// TODO Auto-generated constructor stub
	}
	
	private Rank rank;
	private Suit suit;
	private int value;
	private Object [] card;
	
	public int compareTo(Card other) {
		if (this.getRank().getValue() < other.getRank().getValue()) {
			return -1;
		} else if (this.getRank().getValue() > other.getRank().getValue()) {
			return 1;
		} else {
			return 0;
		}
  }
  
	public Rank getRank() {
		return rank;
		
	}
	
	public Suit getSuit() {
		return suit;
	}
	
	public int getValue() {
		if (rank == Rank.DEUCE) {
			value = 2;
		} else if (rank == Rank.THREE) {
			value = 3;
		} else if (rank == Rank.FOUR) {
			value = 4;
		} else if (rank == Rank.FIVE) {
			value = 5;
		} else if (rank == Rank.SIX) {
			value = 6;
		} else if (rank == Rank.SEVEN) {
			value = 7;
		} else if (rank == Rank.EIGHT) {
			value = 8;
		} else if (rank == Rank.NINE) {
			value = 9;
		} else if (rank == Rank.TEN) {
			value = 10;
		} else if (rank == Rank.JACK) {
			value = 11;
		} else if (rank == Rank.QUEEN) {
			value = 12;
		} else if (rank == Rank.KING) {
			value = 13;
		} else if (rank == Rank.ACE) {
			value = 14;
		}
		return value;
	}
	
	public boolean equals(Card other) {
		if (this.getRank() == other.getRank()) {
			return true;
		} else {
			return false;
		}
	}

	public char suitToString() {
		if (this.getSuit() == Suit.CLUBS) {
			return '\u2663';
		} else if (this.getSuit() == Suit.DIAMONDS) {
			return '\u2666';
		} else if (this.getSuit() == Suit.HEARTS) {
			return '\u2665';
		} else if (this.getSuit() == Suit.SPADES) {
			return '\u2660';
		}
		return 0;
	}
	
	public String toString() {
		String rankString = "";
		switch (rank) {
		case DEUCE:
			rankString = "2";
			break;
		case THREE:
			rankString = "3";
			break;
		case FOUR:
			rankString = "4";
			break;
		case FIVE:
			rankString = "5";
			break;
		case SIX:
			rankString = "6";
			break;
		case SEVEN:
			rankString = "7";
			break;
		case EIGHT:
			rankString = "8";
			break;
		case NINE:
			rankString = "9";
			break;
		case TEN:
			rankString = "10";
			break;
		case JACK:
			rankString = "J";
			break;
		case QUEEN:
			rankString = "Q";
			break;
		case KING:
			rankString = "K";
			break;
		case ACE:
			rankString = "A";
			break;
		}
		return rankString + suitToString();
	}
}