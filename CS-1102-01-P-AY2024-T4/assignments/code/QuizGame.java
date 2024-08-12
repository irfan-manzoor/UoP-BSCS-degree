// import the Scanner class
import java.util.Scanner;

public class QuizGame {
    public static void main(String[] args) {
        // Create a Scanner object to take user input
        Scanner scanner = new Scanner(System.in);
        int score = 0; // Initialize the score counter to 0

        // Define the questions, options, and correct answers
        String[] questions = {
            "Which data structure follows LIFO?", // Q1
            "Which sorting algorithm has O(n log n) average-case time complexity?", // Q2
            "Which language is primarily used for statistical computing?", // Q3
            "What language is used to create web pages?", // Q4
            "Which protocol retrieves email from a server?" // Q5
        };
        String[][] options = {
            // Options for Q1
            {"A) Queue", "B) Stack", "C) Linked List", "D) Tree"},
            // Options for Q2
            {"A) Bubble Sort", "B) Insertion Sort", "C) Merge Sort", "D) Selection Sort"},
            // Options for Q3
            {"A) Java", "B) Python", "C) R", "D) C++"},
            // Options for Q4
            {"A) HTML", "B) HTML", "C) HTTP", "D) HTTPS"},
            // Options for Q5
            {"A) HTTP", "B) FTP", "C) SMTP", "D) POP3"}
        };
        
        // Array containing correct answers for each question
        char[] correctAnswers = {'B', 'C', 'C', 'A', 'D'}; // Correct answers in uppercase

        // Display and process each question
        for (int i = 0; i < questions.length; i++) {
            // Print the question
            System.out.println(questions[i]);
            for (String option : options[i]) {
                // Print the options for the current question
                System.out.println(option);
            }
            // Prompt the user for input
            System.out.print("Enter your answer (A, B, C, or D): ");
            // Read user's answer and convert to uppercase
            char userAnswer = Character.toUpperCase(scanner.next().charAt(0));

            // Compare user's answer with correct answer and update score
            if (userAnswer == correctAnswers[i]) {
                score++; // Increment score if the answer is correct
            }
        }

        // Calculate and display the final score
        // Calculate percentage score
        double percentageScore = (double) score / questions.length * 100;
        // Print the final score
        System.out.println("Your final score: " + percentageScore + "%");

        // Close the scanner object to release resources
        scanner.close(); 
    }
}
