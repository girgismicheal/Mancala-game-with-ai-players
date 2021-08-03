from Board import Board
from choice_player import THE_players
import pickle


class Game():

    def __init__(self):  # two players and board1

        self.player_turn = 0
        self.player1 = None
        self.player2 = None
        self.Curr_Player = None
        self.board = Board()
        self.saved_game=[]

    def Run(self):
        start_or_load = int(input('''
            New Game  ---> Press 1
            Load Game ---> Press 2
        
        '''))
        while start_or_load not in [1,2]:
            start_or_load = int(input('''
            Please Enter a Valid choice!

            New Game  ---> Press 1
            Load Game ---> Press 2
        '''))

        if (start_or_load==1):
            stealing = int(input(
                '''
                1-with Stealing
                2-without Stealing
                '''
            ))
            Game_mode = int(input('''
                    1- Human Vs Human
                    2- Human Vs AI
                    3- AI Vs Human
                    4- AI VS AI
                    Your choice ? :
                    '''))
            if Game_mode>1:
                difficulty=int(input('''
                 1-Easy Mode
                 2-Moderate Mode
                 3-Hard Mode
                '''))
            else:
                difficulty=None
            if Game_mode>1:
                self.player1, self.player2 = THE_players(Game_mode,difficulty)
            else:
                self.player1, self.player2 = THE_players(Game_mode)
            self.Curr_Player = self.player1
            while not self.board.GameOver():
                # print(self.saved_game) ---> this is for testing
                print(f"player : {self.player_turn+1}")
                print(self.board)
                current_state = (self.board, self.player_turn,Game_mode,difficulty, stealing)
                #print(current_state) ---> this is for testing
                with open('saved_gamed', 'wb') as file:
                    pickle.dump(current_state, file)
                file.close()
                # print(type(self.board))
                nextMove = self.Curr_Player.choice(self.board)
                turn_end = self.board.Move(nextMove, self.player_turn, stealing=(stealing==1))
                # change Btween players
                if turn_end:
                    self.player_turn ^= 1
                    if self.player_turn == 0:
                        self.Curr_Player = self.player1
                    else:
                        self.Curr_Player = self.player2
            print(self.board)
            print(f'Player {self.board.who_win()+1} wins !!!!')
            # Todo calc the sum to the nune zero side player
            # rais the winner player
            print('end')
        elif(start_or_load==2):
            with open('saved_gamed', 'rb') as file:
                tuples = pickle.load(file)
            file.close()
           # print(tuples[1])
            #print(tuples)
            self.board,self.player_turn,Game_mode,difficulty, stealing=tuples
            if difficulty is not None:
                self.player1, self.player2 = THE_players(Game_mode,difficulty)
            else:
                self.player1, self.player2 = THE_players(Game_mode)
            if(tuples[1]==0):
                self.Curr_Player = self.player1
            else:
                self.Curr_Player = self.player2
            while not self.board.GameOver():
                # print(self.saved_game) ---> this is for testing
                print(f"player : {self.player_turn+1}")
                print(self.board)
                current_state = (self.board, self.player_turn,Game_mode,difficulty, stealing)
                #self.saved_game.append(current_state)
                with open('saved_gamed', 'wb') as file:
                    pickle.dump(current_state, file)
                file.close()
                # print(type(self.board))
                nextMove = self.Curr_Player.choice(self.board)
                turn_end = self.board.Move(nextMove, self.player_turn, stealing=(stealing==1))
                # change Btween players
                if turn_end:
                    self.player_turn ^= 1
                    if self.player_turn == 0:
                        self.Curr_Player = self.player1
                    else:
                        self.Curr_Player = self.player2
            print(self.board)
            print(f'Player {self.board.who_win()+1} wins !!!!')
            # Todo calc the sum to the nune zero side player
            # rais the winner player
            print('end')


if __name__ == "__main__":
    y='y'
    while y  in ['yes','ya','yeah','Yes','y','Y']:
        game = Game()
        game.Run()
        y=input('do you want to play again?')