class HangmanGame:
    def __init__(self, target_word):
        # We convert the word to Uppercase to make matching easier
        self.secret_word = target_word.upper()
        
        # The player starts with 6 lives
        self.lives_left = 6
        
        # This list will store every letter the user guesses
        self.guessed_letters = []

    def process_guess(self, letter):
        """
        This function takes a letter, checks if it is valid,
        and updates the game state.
        """
        # Convert input to uppercase so 'a' matches 'A'
        letter = letter.upper()

        # 1. Check if the letter was already guessed
        if letter in self.guessed_letters:
            return "ALREADY_GUESSED"
        
        # Add the letter to our list of guesses
        self.guessed_letters.append(letter)

        # 2. Check if the letter is actually in the secret word
        if letter in self.secret_word:
            return "CORRECT"
        else:
            # If wrong, lose a life
            self.lives_left = self.lives_left - 1
            return "WRONG"

    def get_display_word(self):
        """
        This function builds the word to show the user.
        Example: If word is "APPLE" and they guessed "P", 
        it returns "_ P P _ _"
        """
        display_string = ""

        # Loop through every letter in the secret word
        for char in self.secret_word:
            # If the player has guessed this letter, show it
            if char in self.guessed_letters:
                display_string = display_string + char + " "
            # Otherwise, show an underscore
            else:
                display_string = display_string + "_ "
        
        return display_string

    def is_game_over(self):
        """Returns True if lives are 0."""
        if self.lives_left <= 0:
            return True
        else:
            return False

    def is_victory(self):
        """Returns True if all letters in the word have been guessed."""
        # Assume they won, then check if we find any missing letters
        for char in self.secret_word:
            if char not in self.guessed_letters:
                # We found a letter that hasn't been guessed yet
                return False
        
        # If the loop finishes without returning False, they won!
        return True
