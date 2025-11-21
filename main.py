import random
# We import the class we just wrote in the logic folder
from logic.game_engine import HangmanGame

def main():
    print("--- Welcome to the Hangman Project ---")
    
    # TEMPORARY: We will use a simple list for now. 
    # Later, we can connect this to the 'data/words.txt' file.
    word_list = ["PYTHON", "STUDENT", "PROJECT", "COLLEGE", "CODING"]
    
    # Pick a random word
    chosen_word = random.choice(word_list)
    
    # Initialize the game logic class
    game = HangmanGame(chosen_word)

    # Start the Game Loop
    while True:
        # 1. Show current status
        print("\n" + "="*30)
        print("Word to Guess: " + game.get_display_word())
        print("Lives Left: " + str(game.lives_left))
        print("Guessed So Far: " + str(game.guessed_letters))
        
        # 2. Check for Game Over (Loss)
        if game.is_game_over():
            print("\nGAME OVER! You ran out of lives.")
            print("The word was: " + game.secret_word)
            break # Exit the loop
            
        # 3. Check for Victory (Win)
        if game.is_victory():
            print("\nYOU WIN! You guessed the word!")
            break # Exit the loop

        # 4. Get User Input
        guess = input("\nEnter a letter: ")

        # Basic Validation: Ensure they type only 1 letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # 5. Process the guess using our Logic Class
        result = game.process_guess(guess)

        # Give feedback to the user
        if result == "ALREADY_GUESSED":
            print("You already guessed that!")
        elif result == "CORRECT":
            print("Good job! That letter is in the word.")
        elif result == "WRONG":
            print("Sorry, that letter is not there.")

# This line ensures the game runs only when we execute this file directly
if __name__ == "__main__":
    main()
