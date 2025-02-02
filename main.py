from random import randint  # Import randint to randomly determine the answer

def main(games, wins):  
    games += 1  # Increment the number of games played
    print("Guess a number between 1 and 1000\n")  

    answer = randint(1, 1000)  # Generate a random number between 1 and 1000
    attempts = 0  # Initialize the attempt counter

    while attempts < 10:  
        guess = input("Enter your guess: ")  # Get the user's guess

        if guess.lower() == "cheat":  # Cheat mode, reveals the answer
            print("Answer is", answer, end="\n\n")
            continue  # Does not count as an attempt

        try:
            guess = int(guess)  # Convert input to an integer
        except ValueError:  # Catch error if input is not a valid integer
            print("Invalid input! Please enter a valid integer.")
            continue  # Ask for input again without counting an attempt

        attempts += 1  # Increment the attempt counter

        if guess < answer:  # If the guess is too low
            print("Your number is too low")
        elif guess > answer:  # If the guess is too high
            print("Your number is too high")
        else:  # If the guess is correct
            print(f"\nYou won in {attempts} attempts!")
            wins += 1  
            break  # Exit the loop on a win

        print(f"\nOnly {10 - attempts} attempts left!")  # Display remaining attempts

    # If the user has used all 10 attempts without guessing the correct answer
    if attempts == 10 and guess != answer:
        print(f"\nYou lost! The answer was {answer}")

    # Ask the user if they want to play again
    if input("\nPlay again? (y/n): ").strip().lower() == "y":
        print("\n\n------------------------------------------------\n\n")
        main(games, wins)  # Restart the game
    else:
        # Display final game statistics
        print(f"\nYou won {wins} of {games} games, or a {round(wins * 100 / games, 1)}% success rate!")

# Start the game with 0 games played and 0 wins
main(0, 0)
