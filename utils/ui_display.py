import os

HANGMAN_PICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""", 
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""", 
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""", 
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""", 
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""", 
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""", 
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""]

def clear_screen():
    """Clears the terminal screen to make it look neat."""
    if os.name == 'nt': # For Windows
        os.system('cls')
    else: # For Mac/Linux
        os.system('clear')

def print_game_status(lives, display_word, guessed_letters):
    """Prints the stick figure and the current word status."""
    clear_screen()

    pic_index = 6 - lives
    
    print(HANGMAN_PICS[pic_index])
    
    print("\n" + "="*30)
    print("WORD:    " + display_word)
    print("LIVES:   " + str(lives) + "/6")
    print("GUESSES: " + str(guessed_letters))
    print("="*30 + "\n")
