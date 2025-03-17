import random
from bidder_lavrenin import Bidder

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self._User__probability = random.uniform(0, 1)

    def __repr__(self):
        '''User object with secret probability'''
        return f"User(click_probability={self._User__probability:.2f})"

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        return f"User with click probability {self._User__probability:.2f}"

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return random.random() < self._User__probability

class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, num_users, num_bidders, num_rounds):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        self.users = {i: User(i) for i in range(num_users)}  # Pass user_id to User constructor
        self.bidders = {i: Bidder(num_users, num_rounds) for i in range(num_bidders)}
        self.num_rounds = num_rounds
        self.balances = {i: 0 for i in range(num_bidders)}  # Track balances


    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction(users={len(self.users)}, bidders={len(self.bidders)})"

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction with {len(self.users)} users and {len(self.bidders)} bidders"

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
        user_id = random.choice(list(self.users.keys()))
        user = self.users[user_id]

        # Collect bids from bidders (each bidder now has an intelligent strategy)
        bids = {bidder_id: self.bidders[bidder_id].bid(user_id) for bidder_id in self.bidders}
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)

        # Determine winner
        if len(sorted_bids) < 2:
            return  # Need at least 2 bidders

        winner_id = sorted_bids[0][0]
        second_highest_bid = sorted_bids[1][1]

        # Show ad to user and check for a click
        clicked = user.show_ad()

        # Update winner's balance
        if clicked:
            self.balances[winner_id] += 1  # Reward for click
        self.balances[winner_id] -= second_highest_bid  # Deduct second-highest bid
        self.bidders[winner_id].notify(True, second_highest_bid, clicked)

        # Notify other bidders
        for bidder_id in self.bidders:
            if bidder_id != winner_id:
                self.bidders[bidder_id].notify(False, second_highest_bid, None)