from random import randint
import pygame
from pygame import *

display_width = 1500
display_height = 1000

black = (0, 0, 0)
white = (255, 255, 255)

sündmuste_logi = []

pygame.init()  # paneb pygamei mooduli tööle
game_display = pygame.display.set_mode((display_width, display_height))  # display suurus
pygame.display.set_caption("Blackjack")  # display header caption

clock = pygame.time.Clock()  # fpsi jaoks

# image load in section
tagurpidi_kaart_pilt = pygame.image.load("tagurpidikaart.png")  # laeb sisse pildi


#loob teksti objekti, mis võtab sisendiks teksti ja fonti
def text_objects(text, font):
    text_surface = font.render(text, True, black)#loob teksti surface, kus on tekst
    return text_surface, text_surface.get_rect() #returnib teksti surfacei ja sellele vastava teksti ristküliku


#paneb message soovitud asukohta ekraanil
def message_display(text, size, x_asukoht, y_asukoht): # võtab sisendiks teksti, fonti suuruse ja asukohta kuhu message displayda
    display_tekst = pygame.font.Font("freesansbold.ttf", size) # loob muutuja display tekst soovitud fonti ja suurusega
    text_surf, text_rect = text_objects(text, display_tekst) # loob muutuja teksti ristkülik ja teksi surface kasutades teksti objekti funktsiooni
    text_rect.center = (x_asukoht, y_asukoht) # kasutab x_asukohta ja y_asukohta et text paigutada ekraanil soovitud kohta
    game_display.blit(text_surf, text_rect) # paneb ekraanile siis teksti ristküliku ja teksti surfacei




# võtab sisse punktid
def score(punktid):
    message_display(str(punktid[0]), 20,display_width / 2, display_height * 0.3)  # kutsub funktsiooni message display
    message_display(str(punktid[1]), 20, display_width / 2, display_height * 0.7)

#paigutab tagurpidise kaardi ekraanile
def tagurpidi_kaart():
    x = (display_width * 0.1)
    y = (display_height * 0.4)
    game_display.blit(tagurpidi_kaart_pilt, (x, y))

def sündmused(sündmuse_tekst):
    väljastus_tekst = ""
    #
    # if len(sündmuste_logi) < 6:
    #     sündmuste_logi.append(sündmuse_tekst)
    # else:
    #     sündmuste_logi.pop(0)
    #     sündmuste_logi.append(sündmuse_tekst)
    #
    # for elem in sündmuste_logi:
    #     väljastus_tekst += elem + "\n"

    message_display(sündmuse_tekst, 20, display_width * 0.9, display_height * 0.3)





def game_loop():
    crashed = False  # kui true, siis exitib mängust

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # kui sulgeme, siis paneb programmi kinni
                crashed = True

            print(event)

        game_display.fill(white)

        tagurpidi_kaart()
        score([ 0,20])
        sündmused("TA SKOORIB ")
        pygame.display.update()  # updateb ekraanil toimuvat

        clock.tick(60)


game_loop()
pygame.quit()
quit()

pakk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        14] * 4  # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

# Trackib mängu jooksul ai ja mängija kaarte
player = []
computer = []

# Trackib mängu jooksul ai ja mängija punkte
player_punktid = 0
computer_punktid = 0


# Main event handlemine toimub siin. Mäng jookseb siin
def game():
    player = starting_Hand()
    computer = starting_Hand()
    player_punktid = score(player)
    computer_punktid = score(computer)
    print(player)
    print(computer)
    print(player_punktid)
    print(computer_punktid)


# Funktsioon annab kätte esimesed kaks kaarti
def starting_Hand():
    list = []
    list.append(tõmba_kaart())
    list.append(tõmba_kaart())
    return list


def tõmba_kaart():
    number = randint(1, len(pakk))
    kaart = pakk[number]
    pakk.pop(number)
    return kaart


# Arvutab skoori ja tagastab selle
def score(kaardid):
    punktid = 0
    for i in range(len(kaardid)):
        punktid += kaardid[i]

    return punktid


# def ai():
#
#

# #kui kasutaja valib hit, siis tõmmatakse kaardipakkist kaart (jookseb animatsioon) ja tehakse score arvutus
def hit(käsi):
    käsi.append(tõmba_kaart())
    return käsi


# #Kasutaja jätab käigu vahele AI võib teha käigu
# def stand()
#
# #
# # #Kasutaja saab
# # def doubleDown():
# #
# #
# # #Kui aega jääb, siis panused panna mängu
# # def split():
#
#
# #Kasutaja saab ainult esimesel käigul alla anda (automaatselt alla anda)
# def surrender():
#
#
#
# def ai():


game()
