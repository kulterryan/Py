import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        # we will use a single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        # keep track of winner
        self.current_winner = None

    def print_board(self):
        for row in [self.board[1*3:
            (1+1)*3] for i in range(3)]:
                print('| ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # print number board
        number_board = [[str(i) for i in range(j*3, (
            +1)*3)] for j in range(3)]

        for row in number_board:
            print(' | ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,x) in enumerate(self.board):
        #     # ['x', 'x', '0']
        #     if spot == ' ':
        #         moves.append(i)
        #     return moves
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then assign a letter to square
        if self.board[square] == ' ':
            self.board[square] = letter

            # check for the winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere
        # checking rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1) * 3]
        if all([spot == letter for spot in row]):
            return True
    
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number

        if square %2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diag1[1]]):
                return True
            
            diag2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diag2]):
                return True

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game

    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    # starting letter
    # iterate the game still has empty squares

    while game.empty_squares():
        # got the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # Making A Move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square (square) ' )
            game.print_board()
            print(' ') # just empty line

            # after we made our move, we need to alternate letters

            if game.current_winner:
                if print_game:
                    print(letter + ' winner ')
                return letter

            letter = 'O' if letter == 'X' else 'X' # switches player

        # Pause
        time.sleep(0.9)

    if print_game:
        print("It's a Tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)