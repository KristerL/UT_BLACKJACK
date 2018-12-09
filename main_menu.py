import pygame
from pygame import *
import pygame_handler
import ImageLoad
import logic
import time

# Create different objects, that are necessary objects
# starter class initializes pygame and creates the display object
starter_class = pygame_handler.pygame_starter()

# background image is created using the image loading class
background_image = ImageLoad.Image("main_page.jpeg")
#rules_image = ImageLoad.Image("")
# welcome text is generated using the pygame_text class from pygame_handler
welcome_text = pygame_handler.pygame_text("Welcome to Blackjack!", 100, 675, 250)
rules_header = pygame_handler.pygame_text("Rules page!", 100, 675, 250)
# QUIT button is created using the button class from pygame_handler
quit_button = pygame_handler.button("Quit", 50, 575, 700, 200, 100, (230, 0, 0), (255, 30, 30))
game_start_button = pygame_handler.button("Start", 50, 575, 400, 200, 100, (0, 230, 0), (30, 255, 30))
rules_button = pygame_handler.button("Rules", 50, 575, 550, 200, 100, (0, 0, 230), (30, 30, 255))
menu_button = pygame_handler.button("Menu", 50, 575, 700, 200, 100, (230, 0, 0), (255, 30, 30))


background_image = ImageLoad.Image("test2.jpg")

card_deck = logic.Card_deck()
card_deck.shuffle_deck()

bet_button = pygame_handler.button("Bet", 20, 475, 700, 200, 100, (255, 0, 0), (230, 0, 0))
hit_button = pygame_handler.button("Hit", 20, 175, 700, 200, 100, (255, 0, 0), (230, 0, 0))
hit_button1 = pygame_handler.button("Hit", 20, 75, 700, 200, 100, (255, 0, 0), (230, 0, 0))
surrender_button = pygame_handler.button("Surrender", 20, 775, 700, 200, 100, (255, 0, 0), (230, 0, 0))
stand_button = pygame_handler.button("Stand", 20, 1075, 700, 200, 100, (255, 0, 0), (230, 0, 0))
player_info = logic.Player(card_deck)
ai_info = logic.Player(card_deck)

def display_hand(hand_list, height = 10):
    i = 0
    if i < 9:
        for card in hand_list:
            starter_class.game_display.blit(ImageLoad.Image("cardClubs" + str(card)).get_image(), (10 + 150 * i, height))
            i+=1


# main menu runs on the menu_loop
def menu_loop():
    # if crashed, the menu will exit
    crashed = False
    # after exiting, screen will be retured, so the main body knows what window to open next
    screen = "menu"
    to_main_page = False
    to_rule_page = False
    to_game_page = False

    while not crashed:
        for event in pygame.event.get():

            if screen == "menu":
                # blit the background on to the display
                starter_class.game_display.blit(background_image.get_image(), (0, 0))
                # put welcome text on the display starter_class.game_display is the canvas
                welcome_text.display(starter_class.game_display)

                to_game_page = game_start_button.display_button(starter_class.game_display)

                to_rule_page = rules_button.display_button(starter_class.game_display)

                # button is created that usually return None type, but after clicking it will return True
                value = quit_button.display_button(starter_class.game_display)

            elif screen == "rule_page":
                starter_class.game_display.blit(background_image.get_image(), (0, 0))


                to_main_page = menu_button.display_button(starter_class.game_display)

            elif screen == "game":
                game_loop()
                crashed = True




            if to_rule_page:
                screen = "rule_page"
                to_rule_page = False
            elif to_main_page:
                screen = "menu"
                to_main_page = False
            elif to_game_page:
                screen = "game"
                to_game_page = False



            # After quitting pygame, it will close
            if event.type == pygame.QUIT or value:
                crashed = True

        # updates the screen
        pygame.display.update()






def game_loop():
    crashed = False
    current_frame = 0

    while not crashed:

        for event in pygame.event.get():

            starter_class.game_display.blit(background_image.get_image(), (0, 0))



            if current_frame == 0:
                player_info = logic.Player(card_deck)
                ai_info = logic.Player(card_deck)
                current_frame += 1

            if current_frame == 1:

                player_bet = logic.Bet(100)
                bet = bet_button.display_button(starter_class.game_display)
                hit = hit_button.display_button(starter_class.game_display)
                surrender = surrender_button.display_button(starter_class.game_display)
                stand = stand_button.display_button(starter_class.game_display)
                display_hand(player_info.get_hand())
                display_hand(ai_info.get_hand()[:1],200)
                if hit:
                    player_info.hit()
                    hit = False
                    time.sleep(3)
                    current_frame += 1
                if bet:
                    player_bet.add_bet(100)
                    bet = False
                if surrender:
                    player_info.decrease_money(player_bet.get_bet())
                    current_frame += 2
                    surrender = False
                if stand:
                    current_frame +=2
                    stand = False


            if current_frame == 2:
                bet = bet_button.display_button(starter_class.game_display)
                hit = hit_button1.display_button(starter_class.game_display)
                stand = stand_button.display_button(starter_class.game_display)
                display_hand(player_info.get_hand())
                display_hand(ai_info.get_hand()[:1], 200)
                if hit:
                    player_info.hit()
                    hit = False
                if bet:
                    player_bet.add_bet(100)
                    bet = False
                if stand:
                    current_frame +=1
                    stand = False


            if current_frame == 3:
                display_hand(player_info.get_hand())
                display_hand(ai_info.get_hand(), 200)
                while ai_info.score() < 17:
                    ai_info.hit()
                    time.sleep(4)
                current_frame +=1

            if current_frame == 4:
                display_hand(player_info.get_hand())
                display_hand(ai_info.get_hand(), 200)




            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()

menu_loop()

# Exits pygame
pygame.display.quit()
pygame.quit()
quit()
