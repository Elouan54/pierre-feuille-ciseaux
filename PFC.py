import random

def play(player_1, player_2) :
    if player_1 == player_2:
        result = 'draw'
    elif (player_1 == 'pierre' and player_2 == 'ciseaux') or (player_1 == 'feuille' and player_2 == 'pierre') or (player_1 == 'ciseaux' and player_2 == 'feuille'):
        result = 'player 1 win'
    else :
        result = 'player 2 win'
    return result

choices = ['pierre', 'feuille', 'ciseaux']
player_1 = choices[random.randint(0, 2)]
player_2 = choices[random.randint(0, 2)]
print(player_1)
print(player_2)

try:
    print(play(player_1, player_2))
except ValueError:
    print("error : " + ValueError)