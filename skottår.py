import sys
import time


player_health=100
def reduce_player_health(damage):
    global player_health
    player_health = player_health - damage



def trap():
    trap_damage = 2
    reduce_player_health(trap_damage)


def poison():
    poison_damage = 3
    reduce_player_health(poison_damage)


def virus():
    virus_damage = 3
    reduce_player_health(virus_damage)