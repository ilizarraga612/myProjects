// Isabelle Lizarraga

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

// In this assignment you are asked to build class probable text that uses java.util.HashMap<Key,Value>
// as an instance variable to help generate probabilistic text that can look like the book
// used as input, hence probable. You can Alice.txt as input.
public class ProbableText {
	public static void main(String[] args) {
		ProbableText rw = new ProbableText("Alice", 6); // 6 is ngram length
		System.out.println();
		rw.printRandom(33);// # characters to print
	}
	// Instance variables

	HashMap<String, ArrayList<Character>> allNgrams;
	StringBuilder book;
	String ngram;
	private String file;
	int ngramLength;
	Scanner scanner;

	// Read file into Stringbuilder
	public void readBook(String fileName) {
		try {
			scanner = new Scanner(new File(fileName));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		book = new StringBuilder();
		while (scanner.hasNextLine()) {
			this.book.append(scanner.nextLine());
			if (scanner.hasNextLine()) {
				this.book.append(" ");
			}
		}
		scanner.close();
	}

	private void createNgrams(int ngramLength) {
		for (int i = 0; i < book.length() - ngramLength; i++) {
			String ngram = book.substring(i, i + ngramLength);
			char follower = book.charAt(i + ngramLength);
			if (!allNgrams.containsKey(ngram)) {
				ArrayList<Character> followers = new ArrayList<>();
				followers.add(follower);
				allNgrams.put(ngram, followers);
			} else {
				ArrayList<Character> followers = allNgrams.get(ngram);
				followers.add(follower);
				allNgrams.put(ngram, followers);
			}
		}
	}

	// Print random text of length i
	private void printRandom(int i) {
		Random generator = new Random();
		int random = generator.nextInt(book.length() - ngramLength);
		ngram = book.substring(random, random + ngramLength);

		StringBuilder out = new StringBuilder();
		int lineLength = 60;

		int wordBegin = 0;
		int wordEnd = 0;
		boolean word = false;

		for (int j = 0; j < i; j++) {
			ArrayList<Character> followers = allNgrams.get(ngram);
			char follower = followers.get(generator.nextInt(followers.size()));
			out.append(follower);
			System.out.print(follower);
			ngram = ngram.substring(1) + follower;

			if (follower == ' ') {
				wordEnd = j;
				word = true;
			} else {
				if (!word) {
					wordBegin = j;
					word = false;
				}
			}

			if (out.length() - wordBegin >= lineLength) {
				if (word) {
					out.setLength(wordEnd + 1);
					j = wordEnd;
					ngram = book.substring(random + j, random + j + ngramLength);
				}
				out.append("\n");
				word = true;
			}

		}
		System.out.print(out.toString());
	}
	// System.out.println();

	public ProbableText(String fileName, int ngramLength) {
		this.file = fileName;
		this.ngramLength = ngramLength;
		allNgrams = new HashMap<>();
		readBook(fileName);
		createNgrams(ngramLength);
		printRandom(33);
		System.out.println();
		printRandom(33);
		System.out.println();
		printRandom(33);

	}
}
