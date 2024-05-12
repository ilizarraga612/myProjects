//@ Isabelle Lizarraga
package model;
import java.util.ArrayList;
import java.util.Collections;

// Stores the pot, deals two cards to all players, always start with a shuffled deck
// Dealer deals five community cards that can be used by all players
// deals
//
// Dealer will collect 2.00 from each player each game



public class Dealer {
	private int pot;
	private ArrayList<Player> players;
	private ArrayList<Card> communityCards;
	private Deck deck;

	public Dealer() {
		pot = 0;
		players = new ArrayList<Player>();
		communityCards = new ArrayList<Card>();
		deck = new Deck();
		deck.shuffle();
	}

	public void deal() {
		if (deck.isEmpty()) {
			deck.shuffle();
		}
		for (Player p : players) {
			p.setCards(new ArrayList<Card>());
			p.getCards().add(deck.deal());
			p.getCards().add(deck.deal());
		}
	}
	

	public void dealCommunityCards() {
		if (deck.isEmpty()) {
			deck.shuffle();
		}
		for (int i = 0; i < 5; i++) {
			communityCards.add(deck.deal());
		}
		for (Player p : players) {
			p.setBestHand(communityCards);
		}
	}
	
	public void clearCommunityCards() {
		communityCards.clear();
	}
	
// rewritten to account for ties and multiple winners and to accurately split the pot
	public ArrayList<Player> determineWinners() {
		ArrayList<Player> winners = new ArrayList<>();
		Player currentWinner = players.get(0);
		PokerHand bestHand = currentWinner.getBestHand();
		winners.add(currentWinner);
		
		for (int i = 1; i < players.size(); i++) {
			Player p = players.get(i);
			PokerHand currentHand = p.getBestHand();
			if (currentHand.compareTo(bestHand) > 0) {
				winners.clear();
				winners.add(p);
				bestHand = currentHand;
			} else if (currentHand.compareTo(bestHand) == 0) {
				winners.add(p);
			}
		}
		if (winners.size() > 1) {
			int splitPot = pot / winners.size();
			for (Player p : winners) {
				p.setChips(p.getChips() + splitPot);
			}
		} else {
			winners.get(0).setChips(winners.get(0).getChips() + pot);
		}
		pot = 0;
		return winners;
	}
	// will return the hand type of the winner
	public Player determineHandType() {
		PokerHand bestHand = null;
		Player winner = null;
		for (Player p : players) {
			if (bestHand == null || p.getBestHand().compareTo(bestHand) > 0) {
				bestHand = p.getBestHand();
				winner = p;
			}
		}
		winner.setChips(winner.getChips() + pot);
		pot = 0;
		return winner;
	}

	public int getPot() {
		return pot;
	}

	public void setPot(int pot) {
		this.pot = pot;
	}

	public ArrayList<Player> getPlayers() {
		return players;
	}

	public void setPlayers(ArrayList<Player> players) {
		this.players = players;
	}

	public ArrayList<Card> getCommunityCards() {
		return communityCards;
	}

	public void setCommunityCards(ArrayList<Card> communityCards) {
		this.communityCards = communityCards;
	}

	public Deck getDeck() {
		return deck;
	}

	public void setDeck(Deck deck) {
		this.deck = deck;
	}

	public void collectAnte() {
		for (Player p : players) {
			p.setChips(p.getChips() - 2);
			pot += 2;
		}
		// TODO Auto-generated method stub
		
	}

	public void addPlayer(Player p) {
		players.add(p);
		// TODO Auto-generated method stub
		
	}

	public Player getWinner() {
		PokerHand bestHand = null;
		Player winner = null;
		for (Player p : players) {
			if (bestHand == null || p.getBestHand().compareTo(bestHand) > 0) {
				bestHand = p.getBestHand();
				winner = p;
			}
		}
		winner.setChips(winner.getChips() + pot);
		pot = 0;
		return winner;
		// TODO Auto-generated method stub
	}
}
