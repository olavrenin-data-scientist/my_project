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
        print(f"Notify called for {self}, auction_winner={auction_winner}, price={price}, clicked={clicked}") 
        # Debug print 
        if auction_winner: 
            print(f"Before: {self.balance}") 
            self.balance -= price 
            if clicked: 
                self.balance += 1 
                print(f"After: {self.balance}") 


