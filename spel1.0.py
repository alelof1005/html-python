import sys
import time
import random


def vapen_namn():
    if välj_vapen == "3":
        return "Revolver"
    elif välj_vapen == "2":
        return "Yxa"
    elif välj_vapen == "1":
        return "Lasergevär"


inventory = []
exp=0


a = 2
b = 0.2
c = 0.08

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)
        

def expadd(expad):
    global exp
    exp = expad + exp


def loot ():
    if len(inventory) == 5:
        print("Du nått full kapacitet i ditt inventory.")
        print("Du måste ta bort ett föremål för att kunna fortsätta")
        print_inventory()
        item_to_drop = int(input("Ange föremålets plats på listan ifrån toppen som du vill ta bort: "))
        inventory.pop(item_to_drop-1)

    lootchance=random.randint (1,100)
    if lootchance >= 90:
        print("Du har fått en guldtacka ifrån att döda monstret\n")
        inventory.append("Guldtacka")   
    elif lootchance >=70:
        print("Du har fått en kortlek ifrån att döda monstret\n")
        inventory.append("Kortlek")
    elif lootchance >=40:
        print("Du har fått ett äpple ifrån att döda monstret\n")
        inventory.append("Äpple")
    elif lootchance >= 10:
        print("Du har fått en påse jordnötter ifrån att döda monstret\n")
        inventory.append("Jordnötts påse")
    elif lootchance >=1:
        print("Du har fått ett tomt godis papper ifrån att döda monstret\n")
        inventory.append("Tomt godis papper")
    print_inventory ()
    expadd(random.randint(1,3))
    print("Antal Xp poäng:")
    print (f"{exp} Xp")
    menu()
    

def menu ():
    while True:
        print("\nMeny välj ett alternativ:")
        print("1. Slåss mot flera rymd monster")
        print("2. Öppna inventory")
        print("3. Xp Butik")
        print("4. Starta om spelet\n")
        menuchoice=input()
        if menuchoice == "1":
            skydda()
        elif menuchoice== "4":
            game()
            break
        elif menuchoice == "2": 
            print_inventory()
        elif menuchoice == "3":
            butik()
        else: 
            print("Försök igen")


def butik ():
    def check_balance():
        print("\nDitt nuvarande XP saldo är: ", exp)


    def purchase(item_cost, item_name):
        global exp
        if len(inventory) == 5:
            print("Du nått full kapacitet i ditt inventory.")
            drop_item = input("Vill du ta bort ett föremål ifrån ditt inventory för att slutföra köpet? (y/n)")
            if drop_item.lower() == 'y':
                print_inventory()
                item_to_drop = int(input("Ange föremålets plats på listan ifrån toppen som du vill ta bort: "))
                inventory.pop(item_to_drop-1)
                inventory.append(item_name)
                exp -= item_cost
                print("Köp slutfört.")
                check_balance()
            else:
                print("Purchase not completed.")
        else:
            inventory.append(item_name)
            exp -= item_cost
            print("Purchase successful.")
            print("Your inventory: ", inventory)
            check_balance()

    
    items = {
        1: {"name": "Mystisk Månsten", "price": 5},
        2: {"name": "Kyber Kristal", "price": 8},
        3: {"name": "Saturnus Frukt", "price": 15},
        4: {"name": "Darth Vaders Mask", "price": 35}
    }

    def print_items():
        print("Här är en lista på föremål till salu:\n")
        for item_number in items:
            print(f"{item_number}. {items[item_number]['name']} : {items[item_number]['price']}")

    check_balance()
    print_items()

    item_number_to_buy = int(input("Ange Nummret På Föremålet Du Vill Köpa:\nSkriv 0 om du vill återvända till meny "))
    if item_number_to_buy in items:
        purchase(items[item_number_to_buy]['price'], items[item_number_to_buy]['name'])
    if item_number_to_buy==0:
        menu()
    else:
        print("Item not found.")

 
def skydda (): 
        global tjuv_health
        tjuv_health= random.randint (50, 70)
        global player_health
        bonus=random.randint(1,10)
        player_health=100+bonus
        print ("\nDu har valt att attackera monstret")
        print ("Du attackerar monstret")
        print(f"Du får en adrenalin kick som ger dig {bonus} extra hp\n")
        while player_health >0 and tjuv_health >0:
            tjuvdmg=random.randint(10,35)
            print (f"Du anfaller tjuven med {vapen_namn()}")
            reduce_tjuv_health(get_damage())
            print (f"Monstret har {tjuv_health}hp kvar")
            print ("Monstret anfaller dig")
            reduce_player_health(tjuvdmg)
            print (f"Du har {player_health} hp kvar\n")
            if tjuv_health <= 0:
               print ("\nGrattis du har vunnit" )
               loot ()
            if player_health <= 0:
              print ("Du har förlorat")
              game ()

def reduce_player_health(damage):
    global player_health
    player_health = player_health - damage
        
def print_inventory ():
    print("\nDitt inventory:")
    inventory 
    for x in inventory:
        print(x)



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
        print ("Du har valt att gömma dig från rymd monstret")
        print ("Vilket rum väljer du att gömma dig på?")
        print ("1. Sovhytt")
        print ("2. Labbet")
        print ("3. Skafferiet")
        välj_rum = input("Välj rum: ")
        if välj_rum == "1":
            print_slow ("Du har valt att gömma dig i en sovhytt\n") 
        elif välj_rum == "2":
            print_slow ("Du har valt att gömma dig i labbet\n") 
        elif välj_rum == "3":
                print_slow ("Du har valt att gömma dig i skafferiet\n")
        print ("Du har ungefär 70 % chans att undvika rymd monstret")
        ab= random.randint (1,3)
        if ab == 2 :
            print("Monstret hittade dig och dödade dig")
            return False
        else:
            print("Du lyckades för tillfället att undvika monstret")
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
            print_slow("Du vaknar upp mitt i din sömn på rymdstationen till larment som går\n") 
            print_slow("Du reser dig upp genast och går direkt till vapenskåpet.\n")
            while True:
                    print_slow("Vilket vapen väljer du? \n")
                    print("1. Laser gevär")
                    print("2. Yxa")
                    print("3. Revolver")
                    global välj_vapen
                    välj_vapen = input("Välj vapen: ")
                    if välj_vapen == "1":
                        print_slow ("Du har valt att använda Lasergevär\n") 
                    elif välj_vapen == "2":
                        print_slow ("Du har valt att använda Yxa\n") 
                    elif välj_vapen == "3":
                        print_slow ("Du har valt att använda Revolver\n") 
                    print_slow ("Du ser ett rymdmonster börjar närma sig , tänker du attackera den eller gömma dig? \n")
                    alternativ1 = input("1.Jag gömmer mig\n2.Jag ska leta upp monstret och utrota den\n")
                    if alternativ1 == "1":  
                        lyckades_gömma = gömma()
                        if lyckades_gömma == True:
                            print("Du har byggt upp modet medans du har gömt dig så du väljer att konfontrera monstret")
                            skydda ()
                        if lyckades_gömma == False:
                            restart = input('Du förlorade, vill du starta om? Y/N: ')
                            if restart == 'N':
                                break
                            elif restart == 'Y':
                                game ()
                    else: 
                        skydda()
                       
game()