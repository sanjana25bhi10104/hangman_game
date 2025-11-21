import os

def load_words_from_file(filepath):
    """
    Reads a text file and returns a list of words.
    """
    words = []
    
    if not os.path.exists(filepath):
        print("Error: The file " + filepath + " was not found.")
        return ["DEFAULT", "WORD", "BANK"]

    try:
        with open(filepath, 'r') as file:
            for line in file:
                clean_word = line.strip()
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
            score = int(data)
            return score
    except:
        return 0

def save_high_score(filepath, new_score):
    """
    Writes the new high score to a file.
    """
    try:
        with open(filepath, 'w') as file:
            file.write(str(new_score))
    except Exception as e:
        print("Could not save high score: " + str(e))
