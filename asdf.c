#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int secretNumber, guess, attempts = 0;
    
    // Initialize random seed based on current time
    srand(time(0));
    
    // Generate a random number between 1 and 100
    secretNumber = rand() % 100 + 1;
    
    printf("===================================\n");
    printf("     WELCOME TO THE NUMBER GAME    \n");
    printf("===================================\n");
    printf("I have chosen a number between 1 and 100.\n");
    printf("Can you guess what it is?\n\n");
    
    // Game loop
    do {
        printf("Enter your guess: ");
        if (scanf("%d", &guess) != 1) {
            printf("Invalid input! Please enter an integer.\n");
            while (getchar() != '\n'); // Clear input buffer
            continue;
        }
        
        attempts++;
        
        if (guess > secretNumber) {
            printf("Too high! Try a lower number.\n\n");
        } else if (guess < secretNumber) {
            printf("Too low! Try a higher number.\n\n");
        } else {
            printf("\nCongratulations! You found the number %d!\n", secretNumber);
            printf("It took you %d attempts to win.\n", attempts);
        }
        
    } while (guess != secretNumber);
    
    printf("===================================\n");
    printf("Thanks for playing!\n");
    
    return 0;
}
