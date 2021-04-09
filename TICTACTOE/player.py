#import library

import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
        
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input Move (0-8): ")

        # return the correct value by trying to cast it to
        # an int, if that slot is not available on the board,
        # show error: invalid move

        try:
            val = int(square)
            if val not in game.available_moves():
                raise ValueError
            # if these are successful, then
            valid_square = True
        except ValueError:
            print("Opps! Error Invalid Square Selected.")
        return val
