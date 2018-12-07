import pygame
import pygame_handler
import ImageLoad

starter = pygame_handler.pygame_starter()

header = pygame_handler.pygame_text("Rules", 100, 675, 250)

menu_button = pygame_handler.button("Menu",20,575, 700, 200, 100, (255,0,0), (230,0,0))

background_image = ImageLoad.Image("main_page.jpeg")

def rule_loop():
    crashed = False
    screen = "rules"

    while not crashed:
        for event in pygame.event.get():

            starter.game_display.blit(background_image.get_image(), (0,0))

            header.display(starter.game_display)

            menu_button.display_button(starter.game_display)

            if event.type == pygame.QUIT:
                crashed = True


            pygame.display.update()

rule_loop()
pygame.display.quit()
pygame.quit()
quit()

