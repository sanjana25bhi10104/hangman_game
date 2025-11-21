import os  # We need this to check if files exist

def load_words_from_file(filepath):
    """
    Reads a text file and returns a list of words.
    """
    words = []
    
    # Check if the file actually exists first
    if not os.path.exists(filepath):
        print("Error: The file " + filepath + " was not found.")
        # Return a default list so the game doesn't crash
        return ["DEFAULT", "WORD", "BANK"]

    try:
        # Open the file in 'read' mode ('r')
        with open(filepath, 'r') as file:
            # Read each line one by one
            for line in file:
                # .strip() removes invisible newlines (\n) and spaces
                clean_word = line.strip()
                # Only add if the line isn't empty
                if len(clean_word) > 0:
                    words.append(clean_word)
        
        return words

    except Exception as e:
        print("An error occurred while reading words: " + str(e))
        return ["ERROR"]

def get_high_score(filepath):
    """
    Reads the high score from a file. Returns 0 if no file exists.
    """
    if not os.path.exists(filepath):
        return 0
    
    try:
        with open(filepath, 'r') as file:
            data = file.read()
            # Convert the text number into an integer
            score = int(data)
            return score
    except:
        # If the file is empty or broken, just return 0
        return 0

def save_high_score(filepath, new_score):
    """
    Writes the new high score to a file.
    """
    try:
        # Open in 'write' mode ('w'). This overwrites the old file.
        with open(filepath, 'w') as file:
            file.write(str(new_score))
    except Exception as e:
        print("Could not save high score: " + str(e))
