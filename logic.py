from random import shuffle


# Handles player money
class Player(object):
    def __init__(self, my_money=1000):
        self.my_money = my_money

    # decreases player money by amount
    def decrease_money(self, money):
        self.my_money = self.my_money - money

    # increases player money by amount
    def increase_money(self, money):
        self.my_money = self.my_money + money

    # returns the amount of money
    def get_money(self):
        return self.my_money


# Class that handles player hand
class Hand(object):
    def __init__(self):
        hand_list = []
        hand_list.append(Card_deck.get_random_card())
        hand_list.append(Card_deck.get_random_card())
        self.hand = hand_list

    # adds a random card from card_deck to hand
    def hit(self):
        self.hand.append(Card_deck.get_random_card())

    # adds a random card from card deck to hand
    def double_down(self):
        self.hand.append(Card_deck.get_random_card())

    # returns the current hand
    def get_hand(self):
        return self.hand

    def score(self):
        score = 0
        for elem in self.hand:
            ##
            print("fix me")


# handles the current bet
class Bet(object):
    def __init__(self, amount):
        self.bet_amount = amount

    # returns the bet amount
    def get_bet(self):
        return self.bet_amount

    # increases the current bet
    def add_bet(self, amount):
        self.bet_amount += amount


# handles the card deck
class Card_deck(object):
    # creates a new deck
    def __init__(self):
        self.card_pack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                          14] * 4

    # shuffles the deck using shuffle form random module
    def shuffle_deck(self):
        shuffle(self.card_pack)

    # removes a specified card from the deck
    def remove_card(self, card):
        self.card_pack.remove(card)

    # returns the card_pack length
    def get_length(self):
        return len(self.card_pack)

    # returns a random card from the card deck
    def get_random_card(self):
        card = self.card_pack.pop()  # since the deck is shuffled we get a random card
        return card


