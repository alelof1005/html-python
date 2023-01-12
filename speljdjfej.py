import sys
import time

a = 2
b = 0.2
c = 0.08


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)
        # time.sleep(0.07)

def skydda():
    print ("Hur ska du attackera?")
    print ("Attacke")
        
def gömma ():  
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
print("Hagelbössa")
print("Yxa")
print("Revolver")
vapen = input("Välj vapen: ")
print (vapen)
print_slow (f"Du har valt att använda {vapen}\n") 
print_slow ("Någon börjar närma sig ditt rum, tänker du kolla vem det är eller gömma dig? \n")
alternativ1 = input("1.Jag gömmer mig\n2.Jag ska leta upp hen och kämpa emot\n")
if alternativ1 == "1": 
    print ("Du har valt att gömma dig")
else:
    print ("Du har valt att skydda dig mot tjuven")
if alternativ1 == "1":  
    gömma()
