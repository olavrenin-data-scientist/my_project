import random
import numpy as np

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.user_clicks = {i: [] for i in range(num_users)}  # Track click history per user
        self.epsilon = 0.1  # Exploration probability
        self.balance = 0  # Ensure each bidder tracks its balance

    def __repr__(self):
       '''Return Bidder object'''
       return f"Bidder(balance={self.balance})"

    def __str__(self):
        '''Return Bidder object'''
        return f"Bidder with balance {self.balance}"

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        if len(self.user_clicks[user_id]) == 0:
            estimated_prob = 0.5  # Default when no data
        else:
            estimated_prob = np.mean(self.user_clicks[user_id])  # Estimate click-through rate
            
            # ε-greedy strategy: Explore with probability ε
        if random.random() < self.epsilon:
            return round(random.uniform(0, 5), 3)  # Explore random bid
        else:
            return round(estimated_prob * 5, 3)  # Exploit estimated probability


    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        if auction_winner and clicked is not None:
            self.user_clicks.setdefault(price, []).append(1 if clicked else 0)
            self.balance -= price  # Deduct winning price
            if clicked:
                self.balance += 1  # Reward for click

