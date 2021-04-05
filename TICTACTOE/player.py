#import library

import math
import random
import game

class Player:
    def __init__(selfm, letter):
        #letter is x or o
        self.letter = letter
        
        # we want all players to get their next move in the given game
        def get_move(self, game):
            pass

class RandomComputerPlayer:
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, move):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(selfm, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_sq = False
        val = None
        while not valid_sq:
            sq = input(self.letter + "\'s turn. Input Move (0-9): ")

        # return the correct value by trying to cast it to
        # an int, if that slot is not available on the board,
        # show error: invalid move

        try:
            val = int(sq)
            if val not in game.available_moves():
                raise ValueError
            # if these are successful, then
            valid_sq = True
        except ValueError:
            print("Opps! Error Invalid Square Selected.")
        return val
        