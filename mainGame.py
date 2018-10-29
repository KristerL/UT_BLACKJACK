from random import randint

pakk = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]*4 # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

#Trackib mängu jooksul ai ja mängija kaarte
player = []
computer = []

#Trackib mängu jooksul ai ja mängija punkte
player_punktid = 0
computer_punktid = 0



#Main event handlemine toimub siin. Mäng jookseb siin
def game():

    player = starting_Hand()
    computer = starting_Hand()
    player_punktid = score(player)
    computer_punktid = score(computer)
    print(player)
    print(computer)
    print(player_punktid)
    print(computer_punktid)


#Funktsioon annab kätte esimesed kaks kaarti
def starting_Hand():
    list = []
    list.append(tõmba_kaart())
    list.append(tõmba_kaart())
    return list

def tõmba_kaart():
    number = randint(1,len(pakk))
    kaart = pakk[number]
    pakk.pop(number)
    return kaart


#Arvutab skoori ja tagastab selle
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
#def ai():


game()