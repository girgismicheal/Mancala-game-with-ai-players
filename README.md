# Mancala Game with AI (human vs Computer)

![mancala-gam](Image/mancala-game.jpg)

The project is an implementation of MiniMax algorithm with alpha-beta prunning in Python 3 for creating AI capable of playing a Mancala game. 


**Helper items:**
- Binary executable is inside "dist" Folder.
- [How to use mancala-game youtube video](https://www.youtube.com/watch?v=EU4LVfRKxXY)

# Table of contents
- Project Brief Description
- Class Diagram of the complete design of our game
- Detailed Description of Classes & Functions
- Board Class
- Players Class
- AI_player Class
- Game Class
- Node Class
- User Guide


# Project Brief Description:

Full implementation of the famous Mancala Game from scratch.<br><br>
**Including 4 Modes of the game:**
1. Human player Vs. Human player
2. Human player Vs. Ai player
3. Ai player Vs. Human player
4. Ai player Vs. Ai player


**Project Features:**
1. The Ai player uses MinMax Algorithm With Alpha-beta
Pruning written from scratch.
2. The project supports the “Stealing Mode“ of Mancala
3. Various difficulties of AI player (Easy, Medium, and Hard).
4. Saving and loading the current game in case of any sudden termination during the game.
5. Various checks on users' input before the game or within the game.
6. Alpha beta optimization.
7. Added timer inside the mini-max algorithm.
8. Added iterative deepening variant of minmax algorithm.
9. MinMax optimization using sorting of children.


# Class Diagram of the complete design of our game
![Class Diagram](Image/Class_Diagram.png)

# Detailed Description of Classes & Functions
**File Architecture**
```
Mancala Game With Ai Players
|
|── Board.py
|── Players.py
|── Game.py
|── Node.py
|── AI_algorithms.py
|── Ml Algorithms.py
|── Choice_player.py
|── README.md
└── Images
```  


## Board Class:
- The Mancala Board is represented by a list of 14 elements
The first 7 elements are for player 1 (6 holes for stones + 1 for mancala
itself) and the other 7 are for player 2.
- The board is always printed on each play ... starting the game with
value 4 in each hole and zeros for mancalas.
- Possible moves function: returns the possible moves for each player,
as player 1 is allowed to play from his side of board, and also the entered played position mustn’t equal 0.

```Python
from copy import deepcopy
start_board = [4] * 6 + [0] + [4]*6 + [0]

class Board():
    def __init__(self, start_board=start_board):
    def Possible_moves(self, player_turn):
    def Move(self, pos, player_turn, stealing=True):
    def who_win(self):
    def score(self, player):
    def GameOver(self):
    def play_game(self):
    def __str__(self):
```
- **Move function:** is the core of playing the game, the function which is
responsible for the basic movement of mancala. At first, passing the entered position by the user, then checking
If it is a valid input, if so a value of 1 added to each neighbor until the
value of the entered position on the board is 0.
- **Stealing mode:**
If stealing mode is on, and at any time there is a hole on the board
which has a value of 1 and the opposite hole on board is not empty, so
add that 1 + the value of the opposite hole’s value and add the result to
the mancala of the player who has a value 1 in his side of the board
and exactly vice versa for the other player if that case ever happened.

- Who_win: a simple check on which player has a higher score on his
mancala, to be the winner of the game.
- Score function: checks if all holes on any side of the board are empty
(the end of the game) and if so, we will add all the holes’ values of the
other side of the board to this player’s side mancala.
This function returns the difference score between the 2 mancalas to
determine who wins.
- GameOver function: just check on the end of the game condition stated
before and calculating the final score in each mancala.
- Play_game function: just applying the logic explained in all the past
functions, Player move then XORING the player turn as the switch play
(player 0 and 1) Then return the final score.




## Players Class
When instantiating an object of player class, it automatically given an id to mark him.
```Python
from AI_algorithms import AlphaBetaAlg
from Node import Node
import time

class player:
    id = 0

    def __init__(self, id):
        self.id = player.id
        player.id += 1

    def choice(self, board):
        pass


class Human_player(player):

    def choice(self, board):
        pos = self.id * 7 + int(input("Enter your choice: "))
        while pos not in board.Possible_moves(self.id):
            pos = self.id * 7 + int(input(
                f"please enter valid choice: from the list {list(map(lambda x: x - (self.id * 7), board.Possible_moves(self.id)))}"))

        return pos

class AI_player(player):
    def __init__(self, id, diff):
        self.id = player.id
        player.id += 1
        self.diff = diff

    def choice(self, board):
        node = Node(self.id, board)
        start_time = time.time()
        for i in range(1,self.diff):
          value, pos = AlphaBetaAlg(start_time, node, depth=i)
        return pos
```
- **Human_player Class:**
Inherit from Player class to be given an id.
Choice function:
Whatever the id of the player (0 or 1) it returns the
position input by the player, and in case entering a
not valid hole position.
This will fire a message to him to enter a valid one
with printing the possible valid moves.
<br><br>
- **AI_player Class:** it also inherits from player class to be given
an id.
<br><br>
- **Choice function:** when creating the AI agent, the user will be
asked about the difficulty level (a Bonus Part) and based on it.
The AI agent will get deeper or shallower in the searched tree
which is made inside the AlphaBetaAlg function “will be
described later”.
The function will print the possible winning value.
Return: position to be played by AI agent.



## AI_player Class
**THE_players function:** Based on the “Game_mode” & “difficulty” input variables
from user, Players are created with their id.
Also, for AI agent, the difficulty input variable will
determine for which depth it will iterate throw the Tree.

```Python
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
```