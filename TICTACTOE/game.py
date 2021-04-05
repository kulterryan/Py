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
        number_board = [[str(i) for i in range[j*3, (j+1)*3] for j in range(3)]]

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
    