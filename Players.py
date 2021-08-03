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


# test part
from Board import Board

# if __name__ == "__main__":
#     P1 = Human_player(0)
#     P2 = Human_player(1)
#     print(P1.id)
#     print(P2.id)
