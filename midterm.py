import re
from collections import Counter

def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    username_counts = Counter()

    for tweet in tweet_list:
        words = tweet.split()  # Split by spaces
        for word in words:
            if word.startswith('@') and 1 < len(word) <= 14:  # Ensure @ and valid length
                username_counts[word] += 1  # Count occurrences
    return dict(username_counts)



def display(deposits, top, bottom, left, right):
    grid = []
    for _ in range(top, bottom):
        row = []
        for _ in range(left, right):
            row.append('-')
        grid.append(row)
    
    for row, col, _ in deposits:
        if top <= row < bottom and left <= col < right:
            grid[row - top][col - left] = 'X'
    
    result = ""
    for row in grid:
        result += ''.join(row) + "\n"
    return result



def tons_inside(deposits, top, bottom, left, right):
    total_tons = 0
    for row, col, size in deposits:
        if top <= row < bottom and left <= col < right:
            total_tons += size
    return total_tons


def birthday_count(dates_list):
    date_counts = {}
    for date in dates_list:
        date_counts[date] = date_counts.get(date, 0) + 1
    
    count = 0
    for occurrences in date_counts.values():
        if occurrences > 1:
            count += (occurrences * (occurrences - 1)) // 2  # Combination formula
    return count



