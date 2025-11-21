import random
import os

from logic.game_engine import HangmanGame

from utils.file_handler import load_words_from_file, get_high_score, save_high_score

def main():
    print("--- Welcome to the Hangman Project ---")

    word_file_path = os.path.join("data", "words.txt")
    score_file_path = os.path.join("data", "high_score.txt")

    current_high_score = get_high_score(score_file_path)
    print("Current High Score: " + str(current_high_score) + " wins.")

    word_list = load_words_from_file(word_file_path)
    
    # Pick a random word
    chosen_word = random.choice(word_list)
    
    # Start the Game Logic
    game = HangmanGame(chosen_word)

    # The Game Loop
    while True:
        print("\n" + "="*30)
        print("Word: " + game.get_display_word())
        print("Lives: " + str(game.lives_left))
        print("Guessed: " + str(game.guessed_letters))
        
        # Check for Loss
        if game.is_game_over():
            print("\nGAME OVER! The word was: " + game.secret_word)
            # If you lose, reset the high score to 0
            save_high_score(score_file_path, 0) 
            break 
            
        # Check for Win
        if game.is_victory():
            print("\nYOU WIN! You guessed the word!")
            # Calculate new score and save it to the file
            new_score = current_high_score + 1
            save_high_score(score_file_path, new_score)
            print("High Score Saved!")
            break 

        # Get User Input
        guess = input("\nEnter a letter: ")

        # Basic Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Process the guess
        result = game.process_guess(guess)

        if result == "ALREADY_GUESSED":
            print("You already guessed that!")
        elif result == "CORRECT":
            print("Correct!")
        elif result == "WRONG":
            print("Wrong guess.")

if __name__ == "__main__":
    main()
