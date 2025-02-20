from itertools import permutations, product
from wordscore import score_word  # Assuming you have this module (define it separately)

class ScrabbleSolver:
    def __init__(self, dictionary_file="sowpods.txt"):  # Make dictionary file configurable
        self.valid_words = self.load_scrabble_dictionary(dictionary_file)

    def load_scrabble_dictionary(self, dictionary_file):
        """Load the Scrabble dictionary from a file."""
        try:
            with open(dictionary_file, "r") as infile:
                return {word.strip().upper() for word in infile}
        except FileNotFoundError:
            print(f"Error: Dictionary file '{dictionary_file}' not found.")
            return set()  # Return an empty set if the file is not found.

    def generate_valid_words(self, rack: str):
        """Generate valid Scrabble words from a rack, handling wildcards."""
        rack = rack.upper()
        wildcards = rack.count('*') + rack.count('?')

        if wildcards == 0:
            return {''.join(p) for i in range(2, len(rack) + 1) for p in permutations(rack, i) if ''.join(p) in self.valid_words}

        possible_words = set()
        wildcard_positions = [i for i, char in enumerate(rack) if char in '*?']

        for replacement in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=len(wildcard_positions)):
            temp_rack = list(rack)
            for i, letter in enumerate(replacement):
                temp_rack[wildcard_positions[i]] = letter

            replaced_rack = "".join(temp_rack)

            for i in range(2, len(replaced_rack) + 1):
                for perm in permutations(replaced_rack, i):
                    word = "".join(perm)
                    if word in self.valid_words:
                        possible_words.add(word)

        return possible_words

    def run_scrabble(self, rack: str):
        """Find valid Scrabble words, score them, and return results."""
        # Input Validation
        if not isinstance(rack, str):
            return "Error: Input must be a string."

        if not all(char.isalpha() or char in ['*', '?'] for char in rack):
            return "Error: Invalid characters in rack. Use A-Z, *, or ?."

        if not (2 <= len(rack) <= 7):
            return "Error: Rack length must be between 2 and 7."

        if rack.count('*') > 2 or rack.count('?') > 2 or rack.count('*') + rack.count('?') > 2:  # Combined check
          return "Error: Maximum of two wildcards allowed (any combination)."

        valid_words = self.generate_valid_words(rack)

        def adjusted_score(word):
            score = 0
            for char in word:
                if char in rack:  # Directly check if character is in rack
                    score += score_word(char)
                elif '*' in rack or '?' in rack:  # Wildcard used
                    score += score_word(char)  # Score as if wildcard was that letter.
                else:
                    return 0 # If letter not present in rack, word is not valid.

            return score

        scored_words = [(adjusted_score(word), word) for word in valid_words if adjusted_score(word) > 0]
        sorted_words = sorted(scored_words, key=lambda x: (-x[0], x[1]))

        return sorted_words, len(sorted_words)