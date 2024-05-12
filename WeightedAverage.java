// Isabelle Lizarraga
// Description: This program reads in five grade components. It then calculates
// the final course average. 

import java.util.Scanner;

public class WeightedAverage {

    public static void main(String[] args) {
        System.out.println("This program computes a final course grade.");
        System.out.print("\n");
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Assignments: ");
        double assignments = keyboard.nextDouble();

        System.out.print(" Attendance: ");
        double attendance = keyboard.nextDouble();

        System.out.print("     Test 1: ");
        double test1 = keyboard.nextDouble();

        System.out.print("     Test 2: ");
        double test2 = keyboard.nextDouble();

        System.out.print("      Final: ");
        double finalExam = keyboard.nextDouble();
        keyboard.close();

        double courseGrade = (0.35 * assignments) + (0.15 * test1) + (0.15 * test2) + (0.20 * finalExam) + (0.15 * attendance);

        double roundedGrade = Math.round(courseGrade * 10.00) /10.00;
        System.out.print("\n");
        
        System.out.println("Final Grade Percentage: " + roundedGrade);
    }
}

