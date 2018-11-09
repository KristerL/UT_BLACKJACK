from random import shuffle

pakk = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4 # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

#Trackib mängu jooksul ai ja mängija kaarte
mängija_kaardid = []
ai_kaardid = []

#Main event handlemine toimub siin. Mäng jookseb siin
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
            else: continue
        while skoor(ai_kaardid) < 17 and skoor(mängija_kaardid) < 22:
            ai_kaardid = hit(ai_kaardid)
        print(võitja(mängija_kaardid,ai_kaardid))
        otsus = input("[E]dasi või [Q]uit").lower()
    exit()


#Funktsioon annab kätte esimesed kaks kaarti
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

#kui kasutaja valib hit, siis tõmmatakse kaardipakkist kaart (jookseb animatsioon) ja tehakse score arvutus
def hit(käsi):
    käsi.append(tõmba_kaart())
    return käsi

#Arvutab skoori ja tagastab selle
def skoor(kaardid):
    punktid = 0
    for kaart in kaardid:
        if kaart == "J" or kaart == "Q" or kaart == "K": punktid += 10
        elif kaart == "A":
            if punktid >= 11:
                punktid += 1
            else: punktid += 11
        else: punktid += kaart

    return punktid

#Näitab käesolevaid kaarte/punkte ja ühte kaarti, mis arvutil on
def näita_seisu(mängija_kaardid, ai_kaardid):
    print("Sul on kaardid "+ str(mängija_kaardid) + " ,andes skoori " + str(skoor((mängija_kaardid))))
    print("Arvutil on üks kaart " + str(ai_kaardid[1]))

#Leiab, kes on võitja ja tagastab tulemuse
def võitja(mängija_kaardid, ai_kaardid):
    m_skoor = skoor(mängija_kaardid)
    a_skoor = skoor(ai_kaardid)

    if m_skoor > 21:
        return("Kaotus! Läksid lõhki.")
    elif a_skoor > 21:
        return("Arvuti läks lõhki")
    elif m_skoor == a_skoor:
        return("Viik! Mõlemale jäi " + str(m_skoor) + " punkti.")
    elif m_skoor > a_skoor:
        return("Võit! Skoor sinul: " + str(m_skoor) + " vs skoor arvutil: " + str(a_skoor))
    elif a_skoor > m_skoor:
        return("Kaotus! Skoor sinul: " + str(m_skoor) + " vs skoor arvutil: " + str(a_skoor))

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





game()