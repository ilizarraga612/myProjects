//@ Isabelle Lizarraga
package model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
/*
 * When sorted, a list of PokerHand objects will be in ascending order.
 */

public class PokerHand implements Comparable<PokerHand> {
	ArrayList<Card> cards;
	private Card highCard;
	private HashMap<Rank, Integer> countMap;
	private ArrayList<Card> tieBreakers;
	private int pairs;
	private ArrayList<Card> pairedCards;
	private int straightFlush;
	private boolean hasHighCard;

	public PokerHand(Card c1, Card c2, Card c3, Card c4, Card c5) {
		cards = new ArrayList<Card>();

		cards.add(c1);
		if (cards.contains(c2)) {
			throw new IllegalArgumentException();
		} else {
			cards.add(c2);
		}
		if (cards.contains(c3)) {
			throw new IllegalArgumentException();
		} else {
			cards.add(c3);
		}
		if (cards.contains(c4)) {
			throw new IllegalArgumentException();
		} else {
			cards.add(c4);
		}
		if (cards.contains(c5)) {
			throw new IllegalArgumentException();
		} else {
			cards.add(c5);
		}

		Collections.sort(cards);
		highCard = getHighestCard(cards);
		countMap = countCards();
		tieBreakers = (ArrayList) cards.clone();
		Collections.sort(tieBreakers);
		Collections.reverse(tieBreakers);
		pairedCards = getPairedCards();
		pairs = getPairs();
		straightFlush = getStraightFlush();
		// TODO: Build class PokerHand, a week long project
	}

	public ArrayList<Card> getPairedCards() {
		ArrayList<Card> pairedCards = new ArrayList<>();
		for (int i = 0; i < 5; i++) {
			pairedCards.add(null);
		}
		return pairedCards;
	}

	public HashMap<Rank, Integer> countCards() {
		HashMap<Rank, Integer> countMap = new HashMap<>();
		for (Card card : cards) {
			Rank rank = card.getRank();
			countMap.put(rank, countMap.getOrDefault(rank, 0) + 1);
		}
		return countMap;
	}

	public int getPairs() {
		int pairCount = 0;
		boolean pair = false;
		boolean threeOfAKind = false;

		Card pairOneCard = null;
		Card pairTwoCard = null;
		Card threeOfAKindCards = null;

		for (Card card : cards) {
			Rank rank = card.getRank();
			int count = countMap.get(rank);
			if (count == 2) {
				pairCount++;
				pair = true;
				if (pairOneCard != null) {
					if (pairOneCard.compareTo(card) < 0) {
						pairTwoCard = pairOneCard;
						pairOneCard = card;
					} else {
						pairTwoCard = card;
					}
				} else {
					pairOneCard = card;
				}

			} else if (count == 3) {
				threeOfAKind = true;
				threeOfAKindCards = card;

			} else if (count == 4) {
				pairedCards.set(0, card);
				return 8;
			}
		}
		pairedCards.set(1, threeOfAKindCards);
		pairedCards.set(2, pairOneCard);
		pairedCards.set(3, pairTwoCard);
		if (pair && threeOfAKind) {
			return 7;
		} else if (threeOfAKind) {
			return 4;
		} else if (pairCount == 4) {
			return 3;
		} else if (pair) {
			return 2;
		}
		return 0;
		// TODO Auto-generated method stub
	}

	public int getStraightFlush() {
		int sameSuit = 1;
		int consecutiveCount = 1;

		for (int i = 0; i < cards.size() - 1; i++) {
			int currentVal = cards.get(i).getValue();
			int nextVal = cards.get(i + 1).getValue();
			if (currentVal + 1 == nextVal) {
				consecutiveCount++;
			}

			Suit currentSuit = cards.get(i).getSuit();
			Suit nextSuit = cards.get(i + 1).getSuit();
			if (currentSuit == nextSuit) {
				sameSuit++;
			}
		}

		int result = 0;
		if (consecutiveCount == cards.size() && sameSuit == cards.size()) {
			result = (highCard.getRank() == Rank.ACE) ? 10 : 9;
		} else if (sameSuit == cards.size()) {
			result = 6;
		} else if (consecutiveCount == cards.size()) {
			result = 5;
		}
		return result;
	}

	private Card getHighestCard(ArrayList<Card> set) {
		return set.get(set.size() - 1);
	}

	private String handTypeHelper() {
		String handType = "";
		if (pairs != 0) {
			switch (pairs) {
			case 2:
				handType = "One Pair";
				break;
			case 3:
				handType = "Two Pair";
				break;
			case 4:
				handType = "Three of a Kind";
				break;
			case 7:
				handType = "Full House";
				break;
			case 8:
				handType = "Four of a Kind";
				break;
			case 11:
				handType = "High Card";
				break;
			default:
				break;
			}
		} else if (straightFlush != 0) {
			switch (straightFlush) {
			case 5:
				handType = "Straight";
				break;
			case 6:
				handType = "Flush";
				break;
			case 9:
				handType = "Straight Flush";
				break;
			case 10:
				handType = "Royal Flush";
				break;
			default:
				break;
			}
		}
		return handType;
	}

	public String handType(boolean hasHighCard) {
		String handType = handTypeHelper();
		if (handType != "") {
			return handType;
		}
		if (hasHighCard) {
			return "High Card";
		}
		return null;
	}
	
	public String getHandType() {
		String handType = handType(hasHighCard);
		if (handType != null) {
			return handType;
		}
		return "High Card";
	}
	
	@Override
	public int compareTo(PokerHand o) {
		int result = 0;
		int otherResult = 0;

		if (this.pairs != 0 && this.pairs == o.pairs) {
			int i = 0;
			while (i < pairedCards.size() - 1 && this.pairedCards.get(i) == null) {
				i++;
			}

			Card thisMatchCard = this.pairedCards.get(i);
			Card otherMatchCard = o.pairedCards.get(i);
			
				if (thisMatchCard.compareTo(otherMatchCard) > 0) {
					result += this.pairs;
					
				} else if (thisMatchCard.compareTo(otherMatchCard) < 0) {
					otherResult += o.pairs;
				}
		} else if (this.pairs > o.pairs) {
			result += this.pairs;
		} else if (this.pairs < o.pairs) {
			otherResult += o.pairs;
		}
		
		if (this.straightFlush > o.straightFlush) {
			result += this.straightFlush;
		} else if (this.straightFlush < o.straightFlush) {
			otherResult += o.straightFlush;
		}
		if (result == otherResult) {
			for (int i = 0; i < this.tieBreakers.size(); i++) {
				Card thisTieBreaker = this.tieBreakers.get(i);
				Card otherTieBreaker = o.tieBreakers.get(i);
				if (thisTieBreaker.compareTo(otherTieBreaker) > 0) {
					result++;
					break;
				} else if (thisTieBreaker.compareTo(otherTieBreaker) < 0) {
					otherResult++;
					break;
				}
			}
		}
		if (result > otherResult) {
			return 1;
		} else if (result < otherResult) {
			return -1;
		} else {
			return 0;
		}
	}

	public void setCards(ArrayList<Card> cards) {
		this.cards = cards;
	}
	
	public String toString() {
		String result = "";
		for (Card card : cards) {
			result += card.toString() + " ";
		}
		return result.trim();
	}
}
