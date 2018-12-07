import pygame
from pygame import *
        #import main_menu
import logic

"""Examples
card_deck = logic.Card_deck()

print(card_deck.get_length())

print(card_deck.get_card_pack())

player_hand = logic.Hand(card_deck)

print(player_hand.get_hand())

player_hand.hit()

print(player_hand.get_hand())

print(card_deck.get_length())

print(card_deck.get_card_pack())
"""

# initialize deck, starting money (default 1000)
card_deck = logic.Card_deck()
card_deck.shuffle_deck()
player_info = logic.Player(card_deck)

# main loop
while player_info.get_money() > 0 and card_deck.get_length() > 4:

    # mängijale peaks kaardid andma selle loopi alguses, aga esimene käsi tuleb juba enne loopi. Probleem?
    # siin loopis print asemel mingi pygame kood


    # if user presses "quit" then break ???

    # show player cards
    print(player_info.get_hand())
    print(card_deck.get_card_pack())

    # ai gets a hand and shows one card
    ai_info = logic.Player(card_deck)
    ai_hand = ai_info.get_hand()
    print(ai_hand[0])

    # betting phase
    bet = input("bet") # pygame....
    player_bet = logic.Bet(bet)
    print(player_bet.get_bet())
