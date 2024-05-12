package model;
import model.Card;
import java.util.ArrayList;
import java.util.Collections;


// Holds 2 0r 7 Cards and can determine the best hand out of 7 cards (from 7 choose 5).
// All players start with 100 dollars in their balance. The dealer will collect 2 dollars from each player each game.
public class Player {
	private ArrayList<Card> cards;
	private PokerHand bestHand;
	private PokerHand currentHand;
	private double chips;
	private String name;

	public Player(String name,Card c1, Card c2) {
		this.name = name;
		cards = new ArrayList<Card>();
		cards.add(c1);
		cards.add(c2);
		chips = 100.0;
	}

	public void setBestHand(ArrayList<Card> communityCards) {
		ArrayList<Card> allCards = new ArrayList<>();
		allCards.addAll(cards);
		allCards.addAll(communityCards);
		ArrayList<PokerHand> hands = new ArrayList<PokerHand>();
		
		for (int i = 0; i < allCards.size(); i++) {
			for (int j = i + 1; j < allCards.size(); j++) {
				for (int k = j + 1; k < allCards.size(); k++) {
					for (int l = k + 1; l < allCards.size(); l++) {
						for (int m = l + 1; m < allCards.size(); m++) {
							PokerHand hand = new PokerHand(allCards.get(i), allCards.get(j), allCards.get(k), allCards.get(l), allCards.get(m));
							hands.add(hand);
						}
						
					}
				}
			}
		}
		Collections.sort(hands);
		bestHand = hands.get(hands.size() - 1);
		currentHand = hands.get(0);
		
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public PokerHand getBestHand() {
		return bestHand;
	}

	public PokerHand getCurrentHand() {
		return currentHand;
	}

	public ArrayList<Card> getCards() {
		return cards;
	}

	public void setCards(ArrayList<Card> cards) {
		this.cards = cards;
	}

	public double getChips() {
		return chips;
		// TODO Auto-generated method stub
	}

	public void setChips(double i) {
		chips = i;
		
	}

}
