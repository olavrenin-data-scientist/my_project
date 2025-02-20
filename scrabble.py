# scrabble.py

from itertools import permutations, product
from wordscore import score_word

def load_scrabble_dictionary():
    """
    Load the SOWPODS dictionary into a set for quick lookup.
    """
    with open("sowpods.txt", "r") as infile:
        return {word.strip().upper() for word in infile.readlines()}

# Global dictionary (fast lookups)
VALID_WORDS = load_scrabble_dictionary()


def generate_valid_words(rack: str):
    """
    Generate all valid Scrabble words from the given rack, considering wildcards (*, ?).
    """
    rack = rack.upper()
    wildcards = rack.count('*') + rack.count('?')

    # If no wildcards, generate normal permutations
    if wildcards == 0:
        return {''.join(p) for i in range(2, len(rack) + 1) for p in permutations(rack, i) if ''.join(p) in VALID_WORDS}

    possible_words = set()
    base_rack = rack.replace('*', '').replace('?', '')  # Remove wildcards

    # Find wildcard positions
    wildcard_positions = [pos for pos, char in enumerate(rack) if char in '*?']
    
    # Generate all possible wildcard replacements (A-Z)
    wildcard_replacements = product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=len(wildcard_positions))

    # Replace wildcards with all letters and generate words
    for replacement in wildcard_replacements:
        temp_rack = list(rack)
        for i, letter in enumerate(replacement):
            temp_rack[wildcard_positions[i]] = letter  # Replace wildcard

        replaced_rack = ''.join(temp_rack)

        # Generate permutations and check dictionary
        for i in range(2, len(replaced_rack) + 1):
            for perm in permutations(replaced_rack, i):
                word = "".join(perm)
                if word in VALID_WORDS:
                    possible_words.add(word)

    return possible_words



def can_form_word(word, rack):
    """
    Check if a word can be formed from the rack, considering wildcards.
    """
    rack_letters = list(rack.replace('*', '').replace('?', ''))  # Remove wildcards
    wildcards = rack.count('*') + rack.count('?')

    for letter in word:
        if letter in rack_letters:
            rack_letters.remove(letter)  # Use a letter from rack
        elif wildcards > 0:
            wildcards -= 1  # Use a wildcard
        else:
            return False  # Not enough letters or wildcards

    return True



def run_scrabble(rack: str):
    """
    Find all valid Scrabble words that can be formed from a given rack.

    Parameters:
    rack (str): The letter tiles available (2-7 characters, A-Z, at most one '*' and one '?').

    Returns:
    tuple: A list of (score, word) tuples sorted by score (descending) and alphabetically, 
           and the total count of valid words.
    """
    # Input validation
    if not all(char.isalpha() or char in ['*', '?'] for char in rack):
        return "Error: Input should only contain letters (A-Z) and at most two wildcards (*, ?)."

    if not (2 <= len(rack) <= 7):
        return "Error: The letter rack should contain between 2 and 7 characters."

    if rack.count('*') > 1 or rack.count('?') > 1:
        return "Error: A maximum of one '*' and one '?' wildcard is allowed."

    # Generate valid words
    valid_words = generate_valid_words(rack)

    # Compute scores, treating wildcards as 0 points
    def adjusted_score(word):
        """Compute the Scrabble score, treating wildcards as 0 points."""
        score = score_word(word)
        for char in rack:
            if char in '*?':
                score -= score_word(char)  # Deduct wildcard points
        return max(0, score)

    scored_words = [(adjusted_score(word), word) for word in valid_words]

    # Sort by score (descending) and then alphabetically
    sorted_words = sorted(scored_words, key=lambda x: (-x[0], x[1]))

    return sorted_words, len(sorted_words)
