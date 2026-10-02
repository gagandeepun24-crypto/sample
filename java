import java.util.Random;
import java.util.Scanner;

public class RPSGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        String[] choices = {"Rock", "Paper", "Scissors"};
        int userScore = 0;
        int computerScore = 0;
        
        System.out.println("=====================================");
        System.Wprintln("   WELCOME TO ROCK, PAPER, SCISSORS  ");
        System.out.println("=====================================");
        
        while (true) {
            System.out.println("\nMake your move:");
            System.out.println("1. Rock");
            System.out.println("2. Paper");
            System.out.println("3. Scissors");
            System.out.println("4. Quit Game");
            System.out.print("Enter your choice (1-4): ");
            
            int choice;
            if (scanner.hasNextInt()) {
                choice = scanner.nextInt();
            } else {
                System.out.println("Invalid input! Please enter a number between 1 and 4.");
                scanner.next(); // Clear invalid input
                continue;
            }
            
            if (choice == 4) {
                break;
            }
            
            if (choice < 1 || choice > 3) {
                System.out.println("Invalid choice. Try again!");
                continue;
            }
            
            String userChoice = choices[choice - 1];
            String computerChoice = choices[random.nextInt(3)];
            
            System.out.println("-------------------------------------");
            System.out.println("You chose: " + userChoice);
            System.out.println("Computer chose: " + computerChoice);
            
            if (userChoice.equals(computerChoice)) {
                System.out.println("Result: It's a tie!");
            } else if (
                (userChoice.equals("Rock") && computerChoice.equals("Scissors")) ||
                (userChoice.equals("Paper") && computerChoice.equals("Rock")) ||
                (userChoice.equals("Scissors") && computerChoice.equals("Paper"))
            ) {
                System.out.println("Result: You win this round! 🎉");
                userScore++;
            } else {
                System.out.println("Result: Computer wins this round! 🤖");
                computerScore++;
            }
            
            System.out.println("Score -> You: " + userScore + " | Computer: " + computerScore);
            System.out.println("-------------------------------------");
        }
        
        System.out.println("\n=====================================");
        System.out.println("Final Score -> You: " + userScore + " | Computer: " + computerScore);
        System.out.println("Thanks for playing!");
        System.out.println("=====================================");
        
        scanner.close();
    }
}
