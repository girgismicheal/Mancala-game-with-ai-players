from copy import deepcopy

start_board = [4] * 6 + [0] + [4]*6 + [0]


class Board():

    def __init__(self, start_board=start_board):
        # self.player_turn = 0
        self.Board = deepcopy(start_board)

    def Possible_moves(self, player_turn):

        possible_movements = list()
        for index, value in enumerate(self.Board[player_turn * 7:player_turn * 7 + 6]):
            if value != 0:
                possible_movements.append(player_turn * 7 + index)
            # print(possible_moves)
        return possible_movements

    def Move(self, pos, player_turn, stealing=True):
        # while porgram board has not ended

        # pos = player_turn * 7 + int(input("Enter your choice: "))
        # while pos not in self.Possible_moves(player_turn):
        #     pos = player_turn * 7 + int(input(
        #         f"please enter valid choice: from the list {list(map(lambda x: x - (player_turn * 7), self.Possible_moves(player_turn)))}"))


        if pos in self.Possible_moves(player_turn):
            hand = self.Board[pos]
            self.Board[pos] = 0
            # print(hand)
            while hand != 0:
                pos = (pos + 1) % 14
                self.Board[pos % 14] += 1
                hand -= 1

        if stealing and self.Board[pos] == 1 and self.Board[abs(12 - pos)] != 0 and pos not in [6, 13]:
            if player_turn == 0 and pos in [1, 2, 3, 4, 5]:
                self.Board[6] += self.Board[pos] + self.Board[abs(12 - pos)]
                self.Board[pos] = 0
                self.Board[abs(12 - pos)] = 0
            elif (player_turn == 1) and (pos in [8, 9, 10, 11, 12]):
                self.Board[13] += self.Board[pos] + self.Board[abs(12 - pos)]
                self.Board[pos] = 0
                self.Board[abs(12 - pos)] = 0

        if (pos == 6 and player_turn == 0) or (pos == 13 and player_turn == 1):
            return False
        return True

    def who_win(self):
        return 0 if self.Board[6] > self.Board[13] else 1

    def score(self, player):
        if all(ele == 0 for ele in self.Board[0:6]):
            self.Board[13] += self.Board[7] + self.Board[8] + self.Board[9] \
                + self.Board[10] + self.Board[11] + self.Board[12]
            self.Board[7:13] = [0] * 6
        elif all(ele == 0 for ele in self.Board[7:13]):
            self.Board[6] += self.Board[0] + self.Board[1] + self.Board[2] \
                + self.Board[3] + self.Board[4] + self.Board[5]
            self.Board[0:6] = [0] * 6
        score = self.Board[6] - \
            self.Board[13] if player == 0 else self.Board[13] - self.Board[6]
        return score

    def GameOver(self):
        if all(ele == 0 for ele in self.Board[0:6]):
            self.Board[13] += self.Board[7] + self.Board[8] + self.Board[9] + self.Board[10] + self.Board[11] + \
                self.Board[12]
            print(self)
            self.Board[7:13] = [0] * 6
            return True
        elif all(ele == 0 for ele in self.Board[7:13]):
            self.Board[6] += self.Board[0] + self.Board[1] + self.Board[2] + self.Board[3] + self.Board[4] + self.Board[
                5]
            print(self)
            self.Board[0:6] = [0] * 6
            return True

        return False

    def play_game(self):
        while not self.GameOver():
            print(self)
            turn_end = self.Move()
            if turn_end:
                self.player_turn ^= 1
            print(self)

        return self.score()

    def __str__(self):
        # player num : {self.player_turn}
        board_shape = f"""
              5| 4| 3| 2| 1| 0|
          [{self.Board[13]}] {self.Board[12:6:-1]}
              {self.Board[0:6]} [{self.Board[6]}]
              0| 1| 2| 3| 4| 5|
          """
        return board_shape
