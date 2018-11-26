import pygame

# screen size is defined here
display_width = 1350
display_height = 900


# Initilaizes the pygame module and creates the canvas
class pygame_starter():
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((display_width, display_height))  # display canvas
        pygame.display.set_caption("Blackjack")  # display header caption


# Class that handles placing text on screen
class pygame_text():
    # creates a text object using text, fontsize and coordinates
    def __init__(self, text, size=20, x_coord=0, y_coord=0):
        self.text = text
        self.size = size
        self.x_coord = x_coord
        self.y_coord = y_coord

    # Text of the object can be changed, with set_text
    def set_text(self, text):
        self.text = text

    # Text size can be changed
    def set_size(self, size):
        self.size = size

    # Text location can be changed, useful for animation
    def set_location(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    # Displays the object on to our display object
    def display(self, current_display_object):
        diplayed_text = pygame.font.Font("freesansbold.ttf", self.size)  # Font and size
        # Created a surface and a rectangle for the text
        text_surface, text_rectangle = text_objects(self.text, diplayed_text)
        # centers the text rectangle
        text_rectangle.center = (self.x_coord, self.y_coord)
        # puts the text onto the current display object
        current_display_object.blit(text_surface, text_rectangle)


# creates a text object with text and font
def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))  # creates a text surface where the text is
    return text_surface, text_surface.get_rect()  # returns the text surface with its rectangle


# Class for buttons
class button(object):
    def __init__(self, text, font_size, x_coord, y_coord, width, height, inactive_color, active_color, action=None):
        self.text = text
        self.font_size = font_size
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.active = active_color
        self.inactive = inactive_color
        self.action = action

    # function that displays the button
    def display_button(self, current_display_object):
        # tracks mouse movement and clicks
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # if mouse is over the button, it will light up and use active color instead of inactive
        if self.x_coord + self.width > mouse[0] > self.x_coord and self.y_coord + self.height > mouse[1] > self.y_coord:
            pygame.draw.rect(current_display_object, self.active, (self.x_coord, self.y_coord, self.width, self.height))

            if click[0] == 1:
                return True
            # if is clicked, will run the action
            if click[0] == 1 and self.action != None:
                self.action()
                return True
        else:
            pygame.draw.rect(current_display_object, self.inactive,
                             (self.x_coord, self.y_coord, self.width, self.height))

        # creates a text object for the button using pygame_text class that we created
        text = pygame_text(self.text, self.font_size, self.x_coord + self.width / 2, self.y_coord + self.height / 2)
        # Displays the text onto our display object
        text.display(current_display_object)
