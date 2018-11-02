from random import randint

pakk = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4 # kaardipakk on numbritega, et kergemini arvutada skoori, kuigi 11-14 on tegelt pildikaardid

#Trackib mängu jooksul ai ja mängija kaarte
player = []
computer = []

#Trackib mängu jooksul ai ja mängija punkte
player_punktid = 0
computer_punktid = 0



#Main event handlemine toimub siin. Mäng jookseb siin
def game():
    while True:
        print("Vajuta enterit, et mängida 1 käsi või kirjuta exit, et väljuda")
        a = input()
        if a == "exit":
            break

        player = starting_Hand()
        computer = starting_Hand()
        player_punktid = score(player)
        print("Sul on kaardid:",str(player))
        print("Sul on punkte:",str(player_punktid))
        print("Üks arvuti kaartidest on", str(computer[1]))

        #Hittimise tsükkel
        while True:
            otsus = int(input("Vajuta 1, et kaart tõmmata või vajuta 0, et passida"))
            if otsus == 1:
                player = hit(player)
                player_punktid = score(player)
                print("Sul on kaardid:", str(player))
                print("Sul on punkte:", str(player_punktid))
                if player_punktid > 21:
                    pass
                else:
                    continue
            break

        #Vaatab kes võitis
        if player_punktid > 21:
            print("Kaotasid, sest läksid lõhki")
            continue
        kaotus, computer_punktid = ai(computer, player_punktid)
        if kaotus == True:
            print("Arvuti võitis skooriga", str(computer_punktid))
        elif kaotus == False:
            print("Sina võitsid, arvutil jäi punkte", str(computer_punktid))

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
        if kaardid[i] == 14:
            if punktid <= 10:
                punktid += 11
            else:
                punktid += 1
        elif 14 > kaardid[i] > 10:
            punktid += 10
        else:
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
def ai(kaardid, player_punktid):
    punktid = 0
    while True:
        if player_punktid > 21:
            pass
        else:
            punktid = score(kaardid)
            while True:
                if punktid < 17:
                    kaardid = hit(kaardid)
                    punktid = score(kaardid)
                else: break
            if punktid > 21 or punktid < player_punktid:
                return False, punktid
        return True, punktid




game()