
class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        pass

    def __repr__(self):
       '''Return Bidder object'''
       pass

    def __str__(self):
        '''Return Bidder object'''
        pass

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        pass

    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        pass
