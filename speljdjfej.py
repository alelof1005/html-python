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



startGame = input("Would you like to start the game? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
   player = input("Ange ditt namn") 
time.sleep(2)
print_slow("Du vaknar upp mitt i natten till ett ljud av the fönster som krossas\n") 
print_slow("Du reser dig upp genast och går direkt till vapen skåpet")
print_slow("Vilket vapen väljer du")
print("Hagelbössa")
print("Yxa")
print("evolver")