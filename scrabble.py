# scrabble.py

from itertools import permutations, combinations
from wordscore import score_word

def load_scrabble_dictionary():
    with open("sowpods.txt", "r") as infile:
        return {word.strip().upper() for word in infile.readlines()}

VALID_WORDS = load_scrabble_dictionary()

def generate_valid_words(rack: str):
    rack = rack.upper()
    wildcards = rack.count('*') + rack.count('?')

    base_letters = rack.replace('*', '').replace('?', '')

    possible_words = set()

    for i in range(2, len(rack) + 1):
        for perm in permutations(base_letters, i):
            word = "".join(perm)
            if word in VALID_WORDS:
                possible_words.add(word)

    if wildcards > 0:
        for word in VALID_WORDS:
            if can_form_word(word, rack):
                possible_words.add(word)

    return possible_words

def can_form_word(word, rack):
    rack_letters = list(rack.replace('*', '').replace('?', ''))
    wildcards = rack.count('*') + rack.count('?')

    for letter in word:
        if letter in rack_letters:
            rack_letters.remove(letter) 
        elif wildcards > 0:
            wildcards -= 1 
        else:
            return False 

    return True

def run_scrabble(rack: str):
    if not all(char.isalpha() or char in ['*', '?'] for char in rack):
        return "Error: Input should only contain letters (A-Z) and at most two wildcards (*, ?)."

    if not (2 <= len(rack) <= 7):
        return "Error: The letter rack should contain between 2 and 7 characters."

    if rack.count('*') > 1 or rack.count('?') > 1:
        return "Error: A maximum of one '*' and one '?' wildcard is allowed."

    valid_words = generate_valid_words(rack)

    scored_words = [(score_word(word), word) for word in valid_words]

    sorted_words = sorted(scored_words, key=lambda x: (-x[0], x[1]))

    return sorted_words, len(sorted_words)