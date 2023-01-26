import sys
import time
import random
# from pynput.keyboard import Key, Listener

inventory = []
välj_vapen = ""

a = 2
b = 0.2
c = 0.08

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)
        # time.sleep(0.07)

def menu ():
    while True:
        print("Meny välj ett alternativ:")
        print("1. Slåss mot fler tjuvar")
        print("2. Starta om spelet")
        print("3. Öppna inventory")
        menuchoice=input()
        if menuchoice == "1":
            (tjuv_fight)
            break
        elif menuchoice== "2":
            game()
            break
        elif menuchoice == "3": 
            print_inventory()
            
        else: 
            print("Försök igen")


def print_inventory ():
    print("Ditt inventory:")
    inventory = ["Snickers", "Vatten", vapen_namn(), "Skyddsväst\n"]
    for x in inventory:
        print(x)
    menu()

#def tjuv_fight ():
 


player_health=100
def reduce_player_health(damage):
    global player_health
    player_health = player_health - damage
 
def skydda ():
    print ("Du har valt att konfrontera tjuven")
    print ("Du attackerar tjuven")
    print (f"Du anfaller tjuven med {vapen_namn()}")
    reduce_tjuv_health(get_damage())
    print (f"Tjuven har {tjuv_health}hp kvar")

def vapen_namn():
    if välj_vapen == "3":
        return "Revolver"
    elif välj_vapen == "2":
        return "Yxa"
    elif välj_vapen == "1":
        return "Hagelbössa"


tjuv_health= random.randint (50, 99)

def reduce_tjuv_health(damage):
    global tjuv_health
    tjuv_health = tjuv_health - damage


AXE_DAMAGE = 15
HAGELBÖSSA_MAXSKADA = 30
REVOLVER = 18

def get_damage():

    if välj_vapen == "2":
        return AXE_DAMAGE
    elif välj_vapen == "1":
        return random.randint(8, HAGELBÖSSA_MAXSKADA)
    elif välj_vapen == "3" :
        return REVOLVER
    
def gömma ():  
        print ("Du har valt att gömma dig")
        print ("Vilket rum väljer du att gömma dig på?")
        print ("1. Sovrum")
        print ("2. Vardagsrum")
        print ("3. Källaren")
        välj_rum = input("Välj rum: ")
        if välj_rum == "1":
            print_slow ("Du har valt att gömma dig i sovrummet\n") 
        elif välj_rum == "2":
            print_slow ("Du har valt att gömma dig i vardagsrummet\n") 
        elif välj_rum == "3":
                print_slow ("Du har valt att gömma dig i källaren\n")
        print ("Du har ungefär 70 % chans att undvika tjuven")
        ab= random.randint (1,3)
        if ab == 2 :
            print("Tjuven hittade dig och dödade dig")
            return False
        else:
            print("Du lyckades för tillfället att undvika tjuven")
            return True
        
            


def game():
    while True:
        startGame = input("Vill du påbörja spelet? (Y/N): ")
        if startGame == "n" or startGame == "N":
            print("Kanske någon annan gång.")
            time.sleep(3)
            break
        elif startGame == "y" or startGame == "Y":
            player = input("Ange ditt namn: ") 
            time.sleep(2)
            print_slow(f"Välkommen {player}!\n")
            print_slow("Du vaknar upp mitt i natten till ett ljud av ett fönster som krossas\n") 
            print_slow("Du reser dig upp genast och går direkt till vapenskåpet.\n")
            while True:
                    print_slow("Vilket vapen väljer du? \n")
                    print("1. Hagelbössa")
                    print("2. Yxa")
                    print("3. Revolver")
                    global välj_vapen
                    välj_vapen = input("Välj vapen: ")
                    if välj_vapen == "1":
                        print_slow ("Du har valt att använda Hagelbössa\n") 
                    elif välj_vapen == "2":
                        print_slow ("Du har valt att använda Yxa\n") 
                    elif välj_vapen == "3":
                        print_slow ("Du har valt att använda Revolver\n") 
                    print_slow ("Någon börjar närma sig ditt rum, tänker du kolla vem det är eller gömma dig? \n")
                    alternativ1 = input("1.Jag gömmer mig\n2.Jag ska leta upp han och kämpa emot\n")
                    if alternativ1 == "1":  
                        lyckades_gömma = gömma()
                        if lyckades_gömma == False:
                            restart = input('Du förlorade, vill du starta om? Y/N: ')
                            if restart == 'N':
                                break
                            elif restart == 'Y':
                                continue
                    else: 
                        skydda()
                        if tjuv_health <= 0:
                            print ("Grattis du har vunnit" )
                            break
                        if player_health <= 0:
                            print ("Du har förlorat")
                    print_slow("Du kollar ut genom fönstret och ser att det står flera olika främmande på bilar på uppfarten\n")
                    print_slow("Då inser du att det inte bara handlar om en tjuv\n")
                    print_slow("Du inser att detta kommer bli tufft så du går och hämtar en skyddsväst\n")
                    ofl=random.randint(15,30)
                    player_health2=ofl+player_health
                    print(f"Du använder skyddsvästen och har nu {player_health2}hp")
                    menu()

game()