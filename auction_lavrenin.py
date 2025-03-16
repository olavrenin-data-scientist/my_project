import random

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
    
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        self.users = users  # Dictionary {user_id: user_object}
        self.bidders = bidders  # Dictionary {bidder_id: bidder_object}
        self.balances = {bidder_id: 0 for bidder_id in bidders}  # All bidders start with 0 balance

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
        if len(self.users) < 1 or len(self.bidders) < 2:
            print("Not enough users or bidders to run the auction.")
            return
    
        # Select a random user
        user = random.choice(self.users)

        # Collect bids from bidders
        bids = {bidder: bidder.bid(user) for bidder in self.bidders}
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)

        # Ensure there are at least two valid bids
        if len(sorted_bids) < 2:
            print("Not enough valid bids to determine a winner.")
            return

        # Determine winner and second-highest bid
        winner = sorted_bids[0][0]  # ✅ Use object, not ID
        second_highest_bid = sorted_bids[1][1]

        # Show ad to user and check for a click
        clicked = user.show_ad()

        # Notify the winner and update their balance
        winner.notify(True, second_highest_bid, clicked)

        # Notify the losing bidders
        for bidder in self.bidders:
            if bidder != winner:
                bidder.notify(False, second_highest_bid, None)
        for bidder in self.bidders:
            self.balances[bidder] = bidder.balance  

