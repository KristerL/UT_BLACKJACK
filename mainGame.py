#image credits: main_page: https://unsplash.com/photos/GikVY_KS9vQ


import pygame
from pygame import *
from random import shuffle
import os

pakk = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        14] * 4  # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

pildid = {2: "cardCLubs2",3: "cardCLubs3",4: "cardCLubs4",5: "cardCLubs5",6: "cardCLubs6",7: "cardCLubs7",8: "cardCLubs8",9: "cardCLubs9",10: "cardCLubs10",11: "cardCLubsJ",12: "cardCLubsQ",13: "cardCLubsK",14: "cardCLubsA"}
# Trackib mängu jooksul ai ja mängija kaarte
mängija_kaardid = []
ai_kaardid = []

#Display suurus.
display_width = 1350
display_height = 900

#Värvide rgb väärtused
black = (0, 0, 0)
white = (255, 255, 255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)


#Sündmuste logi hoiab mängu jooksul juhtunud sündmuseid
sündmuste_logi = []

pygame.init()  # paneb pygamei mooduli tööle
game_display = pygame.display.set_mode((display_width, display_height))  # display suurus
pygame.display.set_caption("Blackjack")  # display header caption

clock = pygame.time.Clock()  # fpsi jaoks

# image load in section
tagurpidi_kaart_pilt = pygame.image.load("tagurpidikaart.png")  # laeb sisse pildi
main_menu_pic = pygame.image.load("main_page.jpeg")
other_bg_pic = pygame.image.load("test2.jpg")

# loob teksti objekti, mis võtab sisendiks teksti ja fonti
def text_objects(text, font):
    text_surface = font.render(text, True, black)  # loob teksti surface, kus on tekst
    return text_surface, text_surface.get_rect()  # returnib teksti surfacei ja sellele vastava teksti ristküliku


# paneb message soovitud asukohta ekraanil
def message_display(text, size, x_asukoht, y_asukoht):  # võtab sisendiks teksti, fonti suuruse ja asukohta kuhu message displayda
    display_tekst = pygame.font.Font("freesansbold.ttf", size)  # loob muutuja display tekst soovitud fonti ja suurusega
    text_surf, text_rect = text_objects(text,
                                        display_tekst)  # loob muutuja teksti ristkülik ja teksi surface kasutades teksti objekti funktsiooni
    text_rect.center = (
    x_asukoht, y_asukoht)  # kasutab x_asukohta ja y_asukohta et text paigutada ekraanil soovitud kohta
    game_display.blit(text_surf, text_rect)  # paneb ekraanile siis teksti ristküliku ja teksti surfacei


# võtab sisse punktid
def score(punktid):
    message_display(str(punktid[0]), 30, display_width / 2, display_height * 0.3)  # kutsub funktsiooni message display
    message_display(str(punktid[1]), 30, display_width / 2, display_height * 0.7)


# paigutab tagurpidise kaardi ekraanile
def tagurpidi_kaart():
    x = (display_width * 0.1)
    y = (display_height * 0.4)
    game_display.blit(tagurpidi_kaart_pilt, (x, y))

def main_menu_bg():
    game_display.blit(main_menu_pic, (0, 0))

def other_bg():
    game_display.blit(other_bg_pic, (0, 0))

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
#
# def lae_käed(vastaseKäsi, sinuKäsi):
#     x = 0
#     y = 0
#     for element in vastaseKäsi:
#
#
#
#     x = 0
#     y = 0
#
#     for element in sinuKäsi:

#/////////////////////////////////////////////

#laeb pildi ei tööta
def images_load(pilt):
    pilt = pilt + ".png"
    image = pygame.image.load(pilt)

    return image
# ei tööta
def sulge():
    return True

#///////////////////////////////////////////////

#Nuppude loomise funktsioon, mis võtab sisse sõnumi , x ja y koordinaadid, nupu laiuse ja kõrguse ja nupu värvuse
def button(msg,font_size,x_coord,y_coord,width,height,inactive_color,active_color,action=None):
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    print(click)
    #Kontrollib hiire positsiooni. Kui hiir on nupu peal, siis värvib nupu eredamaks
    if x_coord + width > mouse[0] > x_coord and y_coord + height > mouse[1] > y_coord:
        pygame.draw.rect(game_display, active_color, (x_coord, y_coord, width, height))

        #kui hiirega on klikitud ja action on defineeritud. siis jooksuta see action
        if click[0] == 1 and action != None:
            action()
            return True
    else:
        pygame.draw.rect(game_display, inactive_color, (x_coord, y_coord, width, height))

    #kasutab mesaage_display funktsiooni, et ristküliku peale panna tekst
    message_display(msg, font_size, x_coord + width / 2, y_coord + height / 2)


def mängu_nupud():
    y_asukoht = display_height - 250
    x_asukoht = 0
    button("HIT", 25, x_asukoht  , y_asukoht + 50, 200, 50, green, bright_green)
    button("STAND", 25, x_asukoht , y_asukoht + 100, 200, 50, green, bright_green)
    button("DOUBLE DOWN", 25, x_asukoht , y_asukoht +150, 200, 50, green, bright_green)
    button("MENÜÜ", 25, x_asukoht , y_asukoht + 200, 200, 50, green, bright_green, menu)
    button("BET 10", 25, x_asukoht + 225, y_asukoht + 50, 200, 50, green, bright_green)
    button("BET 25", 25, x_asukoht+ 225, y_asukoht + 100, 200, 50, green, bright_green)
    button("BET 50", 25, x_asukoht+ 225, y_asukoht + 150, 200, 50, green, bright_green)
    button("BET 100", 25, x_asukoht+ 225, y_asukoht + 200, 200, 50, green, bright_green)

def kaartide_arv():
    #sama x ja y mis tagurpidi kaart
    x = (display_width * 0.1)
    y = (display_height * 0.4)
    message_display("Kaarte kaardipakis: 0", 20, x + 70, y + 270)
#Displayb menüü

def raha():
    message_display("Raha alles: 0", 30, 150, 50)
    message_display("Praegune panus: 0 ", 30,150,100,)
def menu():
    crashed = False

#main loop, mis jookseb niikaua, kuni crashed = false
    while crashed != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # kui sulgeme, siis paneb programmi kinni
                crashed = True


        game_display.fill(white)
        main_menu_bg()
        message_display("Tere tulemast Blackjacki!", 100, display_width / 2 , display_height / 3);

#Nuppude positsiooni arvutan siin
        rect_x_pos = display_width / 2 - 100
        rect1_y_pos = display_height / 2 - 50
        rect2_y_pos = display_height / 2 + 100
#Loon kaks nuppu button funktsiooni abil
        button("Play",50,rect_x_pos, rect1_y_pos, 200, 100, green,bright_green, game_loop)
        button("Rules",50,rect_x_pos, rect2_y_pos, 200, 100, red,bright_red, rules_leht)

        button("Quit", 50, rect_x_pos, display_height / 2 + 250, 200, 100, red, bright_red)

        #updatein ekraani
        pygame.display.update();

def rules_leht():
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True


        game_display.fill(white)
        other_bg()
        message_display("Reeglid", 75, display_width / 2, display_height / 4)

        button("Menüü", 50, display_width / 2 -100, display_height -150, 200, 100 , green, bright_green, menu)

        pygame.display.update()


def game_loop():
    crashed = False  # kui true, siis exitib mängust

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # kui sulgeme, siis paneb programmi kinni
                crashed = True

            print(event)

        game_display.fill(white)
        other_bg()

        tagurpidi_kaart()
        score([0, 20])
        sündmused("sündmus")
        mängu_nupud()
        kaartide_arv()
        raha()
        pygame.display.update()  # updateb ekraanil toimuvat

        clock.tick(60)


menu()
pygame.display.quit()
pygame.quit()
quit()


# Main event handlemine toimub siin. Mäng jookseb siin
def game():
    otsus = 0
    while otsus != "q":
        if otsus != "h":
            mängija_kaardid = käsi()
            ai_kaardid = käsi()
            näita_seisu(mängija_kaardid, ai_kaardid)
        otsus = input("[H]it, [S]tand").lower()
        if otsus == "h":
            mängija_kaardid = hit(mängija_kaardid)
            näita_seisu(mängija_kaardid, ai_kaardid)
            if skoor(mängija_kaardid) > 21:
                pass
            else:
                continue
        while skoor(ai_kaardid) < 17 and skoor(mängija_kaardid) < 22:
            ai_kaardid = hit(ai_kaardid)
        print(võitja(mängija_kaardid, ai_kaardid))
        otsus = input("[E]dasi või [Q]uit").lower()
    exit()


# Funktsioon annab kätte esimesed kaks kaarti
def käsi():
    kaardid = []
    kaardid.append(tõmba_kaart())
    kaardid.append(tõmba_kaart())
    return kaardid


def tõmba_kaart():
    shuffle(pakk)
    kaart = pakk.pop()
    if kaart == 11: kaart = "J"
    if kaart == 12: kaart = "Q"
    if kaart == 13: kaart = "K"
    if kaart == 14: kaart = "A"

    return kaart


# kui kasutaja valib hit, siis tõmmatakse kaardipakkist kaart (jookseb animatsioon) ja tehakse score arvutus
def hit(käsi):
    käsi.append(tõmba_kaart())
    return käsi


# Arvutab skoori ja tagastab selle
def skoor(kaardid):
    punktid = 0
    for kaart in kaardid:
        if kaart == "J" or kaart == "Q" or kaart == "K":
            punktid += 10
        elif kaart == "A":
            if punktid >= 11:
                punktid += 1
            else:
                punktid += 11
        else:
            punktid += kaart

    return punktid


# Näitab käesolevaid kaarte/punkte ja ühte kaarti, mis arvutil on
def näita_seisu(mängija_kaardid, ai_kaardid):
    print("Sul on kaardid " + str(mängija_kaardid) + " ,andes skoori " + str(skoor((mängija_kaardid))))
    print("Arvutil on üks kaart " + str(ai_kaardid[1]))


# Leiab, kes on võitja ja tagastab tulemuse
def võitja(mängija_kaardid, ai_kaardid):
    m_skoor = skoor(mängija_kaardid)
    a_skoor = skoor(ai_kaardid)

    if m_skoor > 21:
        return ("Kaotus! Läksid lõhki.")
    elif a_skoor > 21:
        return ("Arvuti läks lõhki")
    elif m_skoor == a_skoor:
        return ("Viik! Mõlemale jäi " + str(m_skoor) + " punkti.")
    elif m_skoor > a_skoor:
        return ("Võit! Skoor sinul: " + str(m_skoor) + " vs skoor arvutil: " + str(a_skoor))
    elif a_skoor > m_skoor:
        return ("Kaotus! Skoor sinul: " + str(m_skoor) + " vs skoor arvutil: " + str(a_skoor))


game()
