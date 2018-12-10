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

# bet_button = pygame_handler.button("Bet", 20, 475, 700, 200, 100, (255, 0, 0), (230, 0, 0))
# hit_button = pygame_handler.button("Hit", 20, 175, 700, 200, 100, (255, 0, 0), (230, 0, 0))
# hit_button1 = pygame_handler.button("Hit", 20, 75, 700, 200, 100, (255, 0, 0), (230, 0, 0))
# surrender_button = pygame_handler.button("Surrender", 20, 775, 700, 200, 100, (255, 0, 0), (230, 0, 0))
# stand_button = pygame_handler.button("Stand", 20, 1075, 700, 200, 100, (255, 0, 0), (230, 0, 0))
# continue_button = pygame_handler.button("Continue", 20, 1075, 700, 200, 100, (255, 0, 0), (230, 0, 0))

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
                screen = "menu"




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
    current_frame = "phase2"

    player_info = logic.Player(card_deck)
    ai_info = logic.Player(card_deck)



    text1 = ("[H]it, [S]tand, [D]ouble down")
    text2 = ("[Hit, [S]tand")
    text3 = ("[C]ontinue, [Q]uit")
    text4 = ("AI võitis")
    text5 = ("Sina võitsid")
    text6 = ("Viik")
    text_blank = ""
    text_var = text1
    text_var2 = text_blank

    while not crashed:

        player_score = pygame_handler.pygame_text("Score: " + str(player_info.score())   , 30, 350, 450)
        player_balance = pygame_handler.pygame_text("Balance: " + str(player_info.get_money()), 30, 700, 400)
        instructions = pygame_handler.pygame_text(text_var, 30, 350, 800)
        result = pygame_handler.pygame_text(text_var2, 30, 700, 800)

        for event in pygame.event.get():

            starter_class.game_display.blit(background_image.get_image(), (0, 0))

            instructions.display(starter_class.game_display)
            result.display(starter_class.game_display)
            player_score.display(starter_class.game_display)

            player_balance.display(starter_class.game_display)
            display_hand(player_info.get_hand())
            if current_frame != "phase3" and current_frame != "phase4":
                ai_score = pygame_handler.pygame_text("Score: " + str(ai_info.ai_score()), 30, 350, 600)
                display_hand(ai_info.get_hand()[:1], 200)
                ai_score.display(starter_class.game_display)
            else:
                ai_score = pygame_handler.pygame_text("Score: " + str(ai_info.score()), 30, 350, 600)
                display_hand(ai_info.get_hand()[:], 200)
                ai_score.display(starter_class.game_display)


            if current_frame == "phase1":

                player_info = logic.Player(card_deck, player_info.get_money())
                ai_info = logic.Player(card_deck)
                text_var = text1
                current_frame = "phase2"
                pygame.display.update()


            if current_frame == "phase2":
                bet = logic.Bet(100)
                if len(player_info.get_hand()) == 2 and player_info.score() == 21:
                    ai_info.set_hand()
                    bet.add_bet(50)
                    current_frame == "phase3"
                if event.type == KEYDOWN:

                    if event.key == pygame.K_h:
                        if len(player_info.get_hand()) < 10:
                            player_info.hit()
                            text_var = text2
                    if event.key == pygame.K_s:
                        current_frame = "phase3"
                    if event.key == pygame.K_d:
                        bet.add_bet(100)
                        player_info.hit()

                        current_frame = "phase3"

            if current_frame == "phase3":
                for i in range(2):
                    if ai_info.score() < 17 and ai_info.score() < player_info.score():
                        ai_info.hit()



                if player_info.score() > 21 and ai_info.score() <= 21:
                    text_var2 = text4
                    player_info.decrease_money(bet.get_bet())
                elif player_info.score() > 21 and ai_info.score() > 21:
                    text_var2 = text6
                    player_info.increase_money(bet.get_bet())
                elif player_info.score() <= 21 and ai_info.score() > 21:
                    text_var2 = text5
                elif player_info.score() > ai_info.score():
                    text_var2 = text5
                    player_info.increase_money(bet.get_bet())
                    #player_balance_var = player_info.get_money()
                elif player_info.score() < ai_info.score():
                    text_var2 = text4
                    player_info.decrease_money(bet.get_bet())
                    #player_balance_var = player_info.get_money()
                else:
                    text_var2 = text6
                current_frame = "phase4"

            if current_frame == "phase4":
                text_var = text3
                display_hand(ai_info.get_hand()[:], 200)
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        crashed = True
                    elif event.key == K_c:
                        current_frame = "phase1"

            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()

menu_loop()

# Exits pygame
pygame.display.quit()
pygame.quit()
quit()
