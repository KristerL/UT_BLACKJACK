import pygame
from pygame import *
import pygame_handler
import ImageLoad

# Create different objects, that are necessary objects
# starter class initializes pygame and creates the display object
starter_class = pygame_handler.pygame_starter()
# background image is created using the image loading class
background_image = ImageLoad.Image("main_page.jpeg")
# welcome text is generated using the pygame_text class from pygame_handler
welcome_text = pygame_handler.pygame_text("Welcome to Blackjack!", 100, 675, 250)
# QUIT button is created using the button class from pygame_handler
quit_button = pygame_handler.button("Quit", 50, 575, 700, 200, 100, (230, 0, 0), (255, 30, 30))
game_start_button = pygame_handler.button("Start", 50, 575, 400, 200, 100, (0, 230, 0), (30, 255, 30))
rules_button = pygame_handler.button("Rules", 50, 575, 550, 200, 100, (0, 0, 230), (30, 30, 255))


# main menu runs on the menu_loop
def menu_loop():
    # if crashed, the menu will exit
    crashed = False
    # after exiting, screen will be retured, so the main body knows what window to open next
    screen = "quit"

    while not crashed:
        for event in pygame.event.get():

            if screen == "menu":
                crashed = True
                return "menu"

            # blit the background on to the display
            starter_class.game_display.blit(background_image.get_image(), (0, 0))
            # put welcome text on the display starter_class.game_display is the canvas
            welcome_text.display(starter_class.game_display)

            game_start_button.display_button(starter_class.game_display)

            rules_button.display_button(starter_class.game_display)

            # button is created that usually return None type, but after clicking it will return True
            value = quit_button.display_button(starter_class.game_display)
            # if crashed is True, the loop will break
            crashed = value



            # After quitting pygame, it will close
            if event.type == pygame.QUIT:
                crashed = True

        # updates the screen
        pygame.display.update()


menu_loop()

# Exits pygame
pygame.display.quit()
pygame.quit()
quit()
