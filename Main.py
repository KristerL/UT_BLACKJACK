import pygame
from pygame import *
import main_menu
import logic

card_deck = logic.Card_deck()

print(card_deck.get_length())

print(card_deck.get_card_pack())

player_hand = logic.Hand(card_deck)

print(player_hand.get_hand())

player_hand.hit()

print(player_hand.get_hand())

print(card_deck.get_length())

print(card_deck.get_card_pack())










