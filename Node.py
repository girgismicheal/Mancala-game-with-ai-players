from copy import deepcopy


class Node:

    def __init__(self, player, board, pos=None, is_repeated=False):
        self.player = player
        self.Board = board
        self.pos = pos
        self.is_repeated = is_repeated
        self.value = self.Board.score(player)
        self.index = 0

    def get_children(self):
        children = []
        for move in self.Board.Possible_moves(self.player):
            temp = deepcopy(self.Board)
            is_repeated = not temp.Move(move, self.player)
            children.append(Node(self.player, temp, move, is_repeated))
        return children

    def get_opponent_children(self):
        children = []
        for move in self.Board.Possible_moves(self.player ^ 1):
            temp = deepcopy(self.Board)
            is_repeated = not temp.Move(move, self.player ^ 1)
            children.append(Node(self.player, temp, move, is_repeated))
        return children

    def isterminal(self, isPlayer):
        return len(self.get_children()) == 0 if isPlayer else len(self.get_opponent_children()) == 0

    def __iter__(self):
        # return self.children
        return self

    def __next__(self):
        if self.index >= len(self.children):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.children[index]

    def __str__(self):
        # return f"{self.value},{self.children}"
        return f"{self.node_name}"  # ,{self.value})"

    def __repr__(self):
        return f"{self.node_name}"  # ,{self.value})"
