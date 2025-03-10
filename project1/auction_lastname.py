
class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self, user):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        pass

    def __repr__(self):
        '''User object with secret probability'''
        pass

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        pass

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        pass

class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        pass

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        pass

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        pass

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
        pass
