import sys
import time
import random

a = 2
b = 0.2
c = 0.08

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)
        # time.sleep(0.07)

def skydda ():
    print ("Du har valt att konfrontera tjuven")
    print ("Hur ska du göra?")
    print ("1. Attackera")
    print ("2. Du ropar på den främmande varelsen")
    input ("")
    print (f"Du anfaller tjuven med {v")
    reduce_tjuv_health(get_damage())
    print (f"Tjuven har {tjuv_health}hp kvar")

player_health=100
def reduce_player_health(damage):
    global player_health
    player_health = player_health - damage


tjuv_health= random.randint 50, 99
def reduce_tjuv_health(damage):
    global tjuv_health
    tjuv_health = tjuv_health - damage

def attackera (): 
    tjuv_health (vapen)
        

AXE_DAMAGE = 15
HAGELBÖSSA_MAXSKADA = 30
REVOLVER = 18

def get_damage():
    if vapen == "2":
        return AXE_DAMAGE
    elif vapen == "1":
        return random.randint(8, HAGELBÖSSA_MAXSKADA)
    elif vapen == "3" :
        return REVOLVER
    
def gömma ():  
    print ("Du har valt att gömma dig")
    print ("Vilket rum väljer du att gömma dig på?")
    print ("Sovrum, Vardagsrum eller Källaren")
    rum = input ("Välj:")
    print (rum)

startGame = input("Vill du påbörja spelet? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Kanske någon annan gång.")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
   player = input("Ange ditt namn: ") 
time.sleep(2)
print_slow("Du vaknar upp mitt i natten till ett ljud av ett fönster som krossas\n") 
print_slow("Du reser dig upp genast och går direkt till vapenskåpet.\n")
print_slow("Vilket vapen väljer du? \n")
print("1. Hagelbössa")
print("2. Yxa")
print("3. Revolver")
välj_vapen = input("Välj vapen: ")
if välj_vapen == "1":
    print ("Hagelbössa")
elif välj_vapen == "2":
    print ("Yxa")
elif välj_vapen == "3":
    print ("Revolver")

print_slow (f"Du har valt att använda {välj_vapen}\n") 
print_slow ("Någon börjar närma sig ditt rum, tänker du kolla vem det är eller gömma dig? \n")
alternativ1 = input("1.Jag gömmer mig\n2.Jag ska leta upp hen och kämpa emot\n")
if alternativ1 == "1":  
    gömma()
else: skydda()

