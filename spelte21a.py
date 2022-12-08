import sys
import time



import random
import time

#Tracking weapon and player health
player = {"weapon":None, "health": None}

#function for questions avoide repeat 
def ask(question):
    answer = input(question + " [y/n]")
    return answer in ["y", "Y", "Yes", "YES", "yes"]

def game_over():
  print ("You Lose")
#initial question to start
print ("The adventures Of Magical Nadia")

#Question to start game or end game
if ask("Do you wish to embark on this great adventure?"):
  print ("You have accepted the adventure. God Speed my young rass!")
  player["health"] = 100
else:
  print ("You are a coward and shall not in bark on a great adventure!")

#Dic of all the weapons in the game
WEAPONS = {
  "Spear": (3, 10), None:(1,3), "knife":(4,16), "Gun":(16,25), "Glass Bottle":(4,16)
}


#to give the player weapons code
#player["weapon"] = "Spear"


#Enemys type
enemy = {"name":None, "health":None, "attack":None }
Gaint_spider = {"name":"Spider","health":(10), "attack":(7, 10) } 
Dogs = {"name":"Dogs","health": (50), "attack":(4,15)}
Dragon = {"name":"Dragon","health": (150), "attack":(35,45)}

def reduce_health():
  healthcheck = int(player["health"])
  enemyattack = int("enemy_damage")
  player["health"] = healthcheck - enemyattack
  print (player["health"])
  if player["health"] <= 0:
    game_over()
#Function each fight gives random dmg, have a player and enemy, winner and loser

def combat (player, enemy):
    player_damage = random.randint (*WEAPONS[player["weapon"]])
    enemy_damage = random.randint(*enemy["attack"])
    player_win = player_damage >= enemy["health"]
    enemy_win= enemy_damage  >= player["health"]

    return player_damage, player_win , enemy_damage, enemy_win


#Structure of a fight 
Sample_FIGHT = {
"player_damage": "You desperately try to stop the %s for %i damage",
"enemy_damage": "%s gores you for %i damage",
"player_win": "The %s collapses with a thunderous boom",
"enemy_win": "You are squished"
}

# describe the fight in a function

def describe_combat(player, enemy, fight_description,reduce_health):
   player_damage, player_win , enemy_damage, enemy_win = combat(player, enemy)

   print (fight_description["player_damage"] % (enemy["name"], player_damage))
   time.sleep(1.0) 
   print (fight_description["enemy_damage"] % (enemy["name"], enemy_damage) )
   return reduce_health

   if player_win:
      print (fight_description["player_win"] % enemy["name"])
      return True

   if enemy_win:
      print (fight_description["player_win"] % enemy["name"])
      return False

      return None # fight is a draw

fight_result = describe_combat(player, Gaint_spider, Sample_FIGHT, reduce_health)
while fight_result is None:
   describe_combat(player, Gaint_spider, Sample_FIGHT,reduce_health)
if True: 
   print ("You have won the fight")
   print ()
else:
    print("käften")