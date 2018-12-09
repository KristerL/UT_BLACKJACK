import pygame

import pygame_handler
import ImageLoad

import logic

game_screen = pygame_handler.pygame_starter()
background_image = ImageLoad.Image("test2.jpg")

# clock / game speed
clock = pygame.time.Clock()

card_deck = logic.Card_deck()
card_deck.shuffle_deck()

bet_button = pygame_handler.button("Bet", 20, 575, 700, 200, 100, (255, 0, 0), (230, 0, 0))
hit_button = pygame_handler.button("Hit", 20, 275, 700, 200, 100, (255, 0, 0), (230, 0, 0))

def game_loop():


    def game_start(card_deck):
        player_info = logic.Player(card_deck)
        ai_info = logic.Player(card_deck)
        return player_info, ai_info

    crashed = False
    next_frame = 1

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            game_screen.game_display.blit(background_image.get_image(), (0, 0))

            bet = bet_button.display_button(game_screen.game_display)
            hit = hit_button.display_button(game_screen.game_display)

            if next_frame == 1:
                player_info, ai_info = game_start(card_deck)


            card1_player = ImageLoad.Image("cardClubs" + str(player_info.get_hand()[0]))
            card2_player = ImageLoad.Image("cardClubs" + str(player_info.get_hand()[1]))
            card1_ai = ImageLoad.Image("cardClubs" + str(player_info.get_hand()[0]))
            card2_ai = ImageLoad.Image("cardBack_red1")
            game_screen.game_display.blit(card1_player.get_image(), (50, 10))
            game_screen.game_display.blit(card2_player.get_image(), (200, 10))
            game_screen.game_display.blit(card1_ai.get_image(), (50, 200))
            game_screen.game_display.blit(card2_ai.get_image(), (200, 200))

            if hit:
                print("hey")
                player_info.hit()
                card3_player = ImageLoad.Image("cardClubs" + str(player_info.get_hand()[2]))
                game_screen.game_display.blit(card3_player.get_image(), (350, 10))
                next_frame = 1
                hit = False


            if next_frame == 1:
                next_frame = 0
                pygame.display.update()
                clock.tick(30)

game_loop()
pygame.quit()
quit()

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
