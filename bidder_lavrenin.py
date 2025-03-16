import random

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0

    def __repr__(self):
       '''Return Bidder object'''
       return f"Bidder(balance={self.balance})"

    def __str__(self):
        '''Return Bidder object'''
        return f"Bidder with balance {self.balance}"

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        return random.uniform(0, 5)

    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        if auction_winner:
        # Winner pays the second-highest price (price is second-highest bid)
            self.balance -= price
            if clicked:
                # If the user clicked the ad, the winner gets $1 reward
                self.balance += 1
        else:
            # Loser does not pay for the ad (they didn't win)
            if clicked:
                # If the user clicked, losing bidders do not receive any reward
                pass


