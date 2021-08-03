
from Players import Human_player, AI_player, player

def get_difficulty(d):
    return d*2+1

def THE_players(Game_mode,difficulty=3):
    difficulty = get_difficulty(difficulty)
    player.id=0
    if Game_mode == 1:
        print('Human VS Human Mode')
        Player_1, Player_2 = Human_player(0), Human_player(1)

    elif Game_mode == 2:
        print('Human VS Ai Mode')
        Player_1, Player_2 = Human_player(0), AI_player(1,difficulty)

    elif Game_mode == 3:
        print('Ai VS Human Mode')
        Player_1, Player_2 = AI_player(0,difficulty), Human_player(1)

    elif Game_mode == 4:
        print('Ai VS Ai Mode')
        Player_1, Player_2 = AI_player(0, difficulty), AI_player(1,difficulty)
    return Player_1, Player_2

# test
# if __name__ == "__main__":
#   Player_1, Player_2 = THE_players(4)
#   print(type(Player_1))
#   print(type(Player_2))
