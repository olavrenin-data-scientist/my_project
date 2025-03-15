import random
from bidder_lavrenin import Bidder

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self, user_id):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.user_id = user_id
        self.click_probability = random.uniform(0, 1)

    def __repr__(self):
        '''User object with secret probability'''
        return f"User(click_probability={self.click_probability:.2f})"

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        return f"User with click probability {self.click_probability:.2f}"

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return random.random() < self.click_probability

class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, num_users, num_bidders, num_rounds):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        self.users = {i: User(i) for i in range(num_users)}  # Pass user_id to User constructor
        self.bidders = {i: Bidder(num_users, num_rounds) for i in range(num_bidders)}
        self.num_rounds = num_rounds

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

        # Collect bids from bidders
        bids = {bidder_id: bidder.bid(user_id) for bidder_id, bidder in self.bidders.items()}
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)

        # Determine winner
        if len(sorted_bids) < 2:
            return  # Need at least 2 bidders

        winner_id = sorted_bids[0][0]
        second_highest_bid = sorted_bids[1][1]

        # Show ad to user and check for a click
        clicked = user.show_ad()

        # Update winner's balance
        self.bidders[winner_id].notify(True, second_highest_bid, clicked)

        # Notify other bidders
        for bidder_id in self.bidders:
            if bidder_id != winner_id:
                self.bidders[bidder_id].notify(False, second_highest_bid, False)

        # Print round results
        print(f"User {user_id} chosen. Winner: Bidder {winner_id}, Paid: {second_highest_bid}, Clicked: {clicked}")




auction = Auction(num_users=10, num_bidders=5, num_rounds=20)
for _ in range(auction.num_rounds):
    auction.execute_round()

