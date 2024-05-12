//@ Isabelle Lizarraga
package model;

import model.Dealer;
import model.Player;
import model.Deck;
import model.Card;
import model.PokerHand;
import java.util.Scanner;
import java.util.ArrayList;


public class Game {
	
	public Game() {
		Dealer dealer;
		Deck deck;
		dealer = new Dealer();
		deck = new Deck();
		deck.shuffle();
		
		
		Scanner input = new Scanner(System.in);
		System.out.println("How many players will be playing? (2-10)");
		int numPlayers = input.nextInt();
		
		for (int i = 0; i < numPlayers; i++) {
			Player p = new Player("Player " + (i+1),deck.deal(), deck.deal());
			dealer.addPlayer(p);
			
		}
		dealer.collectAnte();
		dealer.deal();
		dealer.dealCommunityCards();
		
		int playerNum = 0;
		

		for (Player p : dealer.getPlayers()) {
			playerNum++;
			p.setBestHand(dealer.getCommunityCards());
			System.out.println("Player " + playerNum + " (Balance: $" + p.getChips() + ") Hand: ");
			for (Card c : p.getCards()) {
				System.out.print(c.toString() + " ");
			}
			System.out.println();
			System.out.println("Best Hand: " + p.getBestHand().toString() + " (" + p.getBestHand().getHandType() + ")");
		}
		System.out.println("Community Cards: ");
		for (Card c : dealer.getCommunityCards()) {
			System.out.print(c.toString() + " ");
		}
		
		System.out.println();
		
		ArrayList<Player> winners = dealer.determineWinners();
		if (winners.size() == 1) {
			Player winner = winners.get(0);
			System.out.println("Winner: " + winner.getName() + " (Balance: $ " + winner.getChips() + ")");
		} else {
			System.out.println("Winners: ");
			for (Player winner : winners) {
				winner.setChips(winner.getChips() + dealer.getPot()/winners.size());
				System.out.println(winner.getName() + " (Balance: $ " + winner.getChips() + ")");
				
            }
			
		} 
		System.out.println("Would you like to play another game? (y/n)");
		
		String playAgain = input.next();
		deck.shuffle();
		
		while (playAgain.equals("y")) {
			deck.shuffle();
			dealer.collectAnte();
			dealer.deal();
			dealer.clearCommunityCards();
			dealer.dealCommunityCards();
			
			for (Player p : dealer.getPlayers()) {
				p.setBestHand(dealer.getCommunityCards());
				System.out.println( p.getName() + " (Balance: $ " + p.getChips() + ") Hand: ");
				for (Card c : p.getCards()) {
					System.out.print(c.toString() + " ");
				}
				System.out.println();
				System.out.println("Best Hand " + p.getBestHand().toString() + " " + " (" + p.getBestHand().getHandType().toString() + ")");
			}
			
			System.out.println("Community Cards: ");
			for (Card c : dealer.getCommunityCards()) {
				System.out.print(c.toString() + " ");
			}
			System.out.println();
			winners = dealer.determineWinners();
			if (winners.size() == 1) {
				Player winner = winners.get(0);
				System.out.println("Winner: " + winner.getName() + " (Balance: $ " + winner.getChips() + ")");
			} else {
				System.out.println("Winners: ");
				for (Player winner : winners) {
					winner.setChips(winner.getChips() + dealer.getPot() / winners.size());
					System.out.println(winner.getName() + " (Balance: $ " + winner.getChips() + ")");
				}
			}
			System.out.println("Would you like to play another game? (y/n)");
			playAgain = input.next();
			// Add the pot to the winning players balance
			}

			input.close();
		}
		// Precondition: Number of players entered will be from 2 min through 10 max


// starts the game by creating a new deck, shuffling it, and creating a new dealer
	public void start() {
		Game theGame = new Game();
		theGame.start();
		// TODO Auto-generated method stub
		
	}

}

