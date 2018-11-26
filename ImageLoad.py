import pygame


# class that handles imageloading
class Image(object):
    # image object is created with using the image name
    def __init__(self, image_name):
        if image_name[0:4] == "card":
            self.image = pygame.image.load("./Images/Cards/" + image_name + ".png")
        else:
            self.image = pygame.image.load("./Images/" + image_name)

    # image object is returned with using this function
    def get_image(self):
        return self.image
