import random
import os
from logic.game_engine import HangmanGame
from utils.file_handler import load_words_from_file, get_high_score, save_high_score
from utils.ui_display import print_game_status

def main():
    word_file_path = os.path.join("data", "words.txt")
    score_file_path = os.path.join("data", "high_score.txt")

    print("Loading game...")
    word_list = load_words_from_file(word_file_path)
    current_high_score = get_high_score(score_file_path)
    
    chosen_word = random.choice(word_list)
    game = HangmanGame(chosen_word)

    print_game_status(game.lives_left, game.get_display_word(), game.guessed_letters)
    print(f"Current High Score: {current_high_score} Wins")

    while True:
        guess = input("Enter a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input! Single letters only.")
            input("Press Enter to try again...") 
            continue

        result = game.process_guess(guess)
        
        print_game_status(game.lives_left, game.get_display_word(), game.guessed_letters)

        # Feedback
        if result == "ALREADY_GUESSED":
            print(">> You already guessed that!")
        elif result == "CORRECT":
            print(">> Good job!")
        elif result == "WRONG":
            print(">> Wrong letter!")

        if game.is_game_over():
            print("\nGAME OVER! The word was: " + game.secret_word)
            save_high_score(score_file_path, 0) 
            break 
            
        if game.is_victory():
            print("\nYOU WIN! You guessed the word!")
            new_score = current_high_score + 1
            save_high_score(score_file_path, new_score)
            print("High Score Updated: " + str(new_score))
            break 

if __name__ == "__main__":
    main()
