from random import randint

pakk = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]*4 # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

#Trackib mängu jooksul ai ja mängija kaarte
player = []
computer = []

#Trackib mängu jooksul ai ja mängija punkte
playerPunktid = 0
computerPunktid = 0



#Main event handlemine toimub siin. Mäng jookseb siin
def game():

    player = start()
    computer = start()
    playerPunktid = score(player)
    computerPunktid = score(computer)
    print(player)
    print(computer)
    print(playerPunktid)
    print(computerPunktid)


#Funktsioon annab kätte esimesed kaks kaarti
def start():
    list = []
    kaart = pakk[randint(1,len(pakk))]
    list.append(kaart)
    kaart = pakk[randint(1,len(pakk))]
    list.append(kaart)

    return list




#Arvutab skoori ja tagastab selle
def score(kaardid):
    punktid = 0
    for j in range(len(kaardid)):
            punktid += kaardid[j]

    return punktid



#
#
# #Kasutaja saab ainult esimesel käigul alla anda (automaatselt alla anda)
# def surrender():
#
#
#
# def ai():
#
#

# #kui kasutaja valib hit, siis tõmmatakse kaardipakkist kaart (jookseb animatsioon) ja tehakse score arvutus
# def hit():
#
#
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