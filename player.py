class player(object):
    def __init__(self):
        self.hand = []

    def sort(self):
        self.hand.sort(key=lambda v: v.vel)
        self.hand.sort(key=lambda v: v.suit)
