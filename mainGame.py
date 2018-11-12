
import pygame
from pygame import *
from random import shuffle

pakk = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4 # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

#Trackib mängu jooksul ai ja mängija kaarte
mängija_kaardid = []
ai_kaardid = []
raha = int(input("Kui suure summaga mängid? "))

"""
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
"""

#Main event handlemine toimub siin. Mäng jookseb siin
def game():
    otsus = 0
    panus = 0
    global raha

    while otsus != "q":

        if len(pakk) <= 6:
            print("Pakist said kaardid otsa, mäng on läbi")
            break

        if otsus != "h":
            mängija_kaardid = käsi()
            ai_kaardid = käsi()
            panus = int(input("Sisesta oma panus: "))
            näita_seisu(mängija_kaardid, ai_kaardid)

            if blackjack(mängija_kaardid,ai_kaardid) == True:
                if skoor(mängija_kaardid) == 21 and skoor(ai_kaardid) == 21:
                    print("Mõlemal on Blackjack!")
                    continue
                elif skoor(mängija_kaardid) == 21:
                    print("Palju Õnne! Sul on Blackjack.")
                    tekst, panus = (võitja(mängija_kaardid, ai_kaardid, panus))
                    print(tekst)
                    raha = raha + panus
                    print("Sul on raha", str(raha))
                    continue
                elif skoor(ai_kaardid) == 21:
                    print("Kahjuks on arvutil Blackjack.")
                    tekst, panus = (võitja(mängija_kaardid, ai_kaardid, panus))
                    print(tekst)
                    raha = raha + panus
                    print("Sul on raha", str(raha))
                    continue
        if otsus == "h":
            otsus = input("[H]it, [S]tand: ").lower()
        else: otsus = input("[H]it, [S]tand, [D]ouble down: ").lower()

        if otsus == "h":
            mängija_kaardid = hit(mängija_kaardid)
            näita_seisu(mängija_kaardid, ai_kaardid)
            if skoor(mängija_kaardid) > 21:
                pass
            else: continue

        elif otsus == "d":
            mängija_kaardid, panus = double_down(mängija_kaardid, panus)
            näita_seisu(mängija_kaardid,ai_kaardid)
            pass

        while skoor(ai_kaardid) < 17 and skoor(mängija_kaardid) < 22:
            ai_kaardid = hit(ai_kaardid)
        tekst, panus = (võitja(mängija_kaardid,ai_kaardid,panus))
        print(tekst)
        raha = raha + panus
        print("Sul on raha", str(raha))
        otsus = input("[E]dasi või [Q]uit").lower()

    print("Tulid mängust ära summaga", str(raha))
    exit()


#Funktsioon annab kätte esimesed kaks kaarti
def käsi():
    kaardid = []
    kaardid.append(tõmba_kaart())
    kaardid.append(tõmba_kaart())
    return kaardid

#Tõmbab pakist ühe kaardi ja lisab selle kätte
def tõmba_kaart():
    shuffle(pakk)
    kaart = pakk.pop()
    if kaart == 11: kaart = "J"
    if kaart == 12: kaart = "Q"
    if kaart == 13: kaart = "K"
    if kaart == 14: kaart = "A"

    return kaart

#Kui kasutaja valib hit, siis tõmmatakse kaardipakkist kaart (jookseb animatsioon) ja tehakse score arvutus
def hit(käsi):
    käsi.append(tõmba_kaart())
    return käsi


#Arvutab skoori ja tagastab selle
def skoor(kaardid):
    if "A" in kaardid and kaardid[-1] != "A":
        a = kaardid.index("A")
        kaardid[a], kaardid[-1] = kaardid[-1], kaardid[a]
    punktid = 0
    for kaart in kaardid:
        if kaart == "J" or kaart == "Q" or kaart == "K": punktid += 10
        elif kaart == "A":
            if punktid >= 11:
                punktid += 1
            else: punktid += 11
        else: punktid += kaart

    return punktid

#Näitab käesolevaid kaarte/punkte, panust ja ühte kaarti, mis arvutil on
def näita_seisu(mängija_kaardid, ai_kaardid):
    print("Sul on kaardid "+ str(mängija_kaardid) + " ,andes skoori " + str(skoor((mängija_kaardid))))
    print("Arvutil on üks kaart " + str(ai_kaardid[1]))

#Leiab, kes on võitja ja tagastab tulemuse
def võitja(mängija_kaardid, ai_kaardid, panus):
    m_skoor = skoor(mängija_kaardid)
    a_skoor = skoor(ai_kaardid)

    if m_skoor > 21:
        return ("Kaotus! Läksid lõhki."), (-panus)
    elif a_skoor > 21:
        return("Arvuti läks lõhki"), (panus)
    elif m_skoor == a_skoor:
        return("Viik! Mõlemale jäi " + str(m_skoor) + " punkti."), 0
    elif m_skoor > a_skoor:
        return("Võit! Skoor sinul: " + str(m_skoor) + " vs skoor arvutil: " + str(a_skoor)), (panus)
    elif a_skoor > m_skoor:
        return("Kaotus! Skoor sinul: " + str(m_skoor) + " vs skoor arvutil: " + str(a_skoor)), (-panus)

def blackjack(käsi1, käsi2):
    if skoor(käsi1) == 21 and skoor(käsi2) == 21:
        return True
    elif skoor(käsi1) == 21:
        return True
    elif skoor(käsi2) == 21:
        return True
    else:
        return False

def double_down(käsi, panus):
    käsi = hit(käsi)
    panus = panus * 2
    return käsi, panus

game()
