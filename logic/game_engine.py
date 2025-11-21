class HangmanGame:
    def __init__(self, target_word):
        self.secret_word = target_word.upper()
        
        self.lives_left = 6
        
        self.guessed_letters = []

    def process_guess(self, letter):
        """
        This function takes a letter, checks if it is valid,
        and updates the game state.
        """
        letter = letter.upper()

        if letter in self.guessed_letters:
            return "ALREADY_GUESSED"
        
        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            return "CORRECT"
        else:
            self.lives_left = self.lives_left - 1
            return "WRONG"

    def get_display_word(self):
        """
        This function builds the word to show the user.
        Example: If word is "APPLE" and they guessed "P", 
        it returns "_ P P _ _"
        """
        display_string = ""

        for char in self.secret_word:
            if char in self.guessed_letters:
                display_string = display_string + char + " "
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
        for char in self.secret_word:
            if char not in self.guessed_letters:
                return False
        
        return True
