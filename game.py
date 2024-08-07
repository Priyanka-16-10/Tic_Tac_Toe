from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        # creating a 3x3 board using a single list
        self.board = [' ' for _ in range(9)] 
        # keep track of the winner
        self.current_winner = None 

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # Fixed the list comprehension for a 3x3 grid
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere...
        
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check the column
        col_ind = square % 3
        col = [self.board[col_ind + i*3] for i in range(3)]  # Corrected range usage
        if all([spot == letter for spot in col]):
            return True

        # check diagonal
        # only if the square is an even number [0, 2, 4, 6, 8]
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # all conditions failed    
        return False

def play(game, x_player, o_player, print_game=True):
    # return the winner of the game or None
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # switch players
            letter = 'O' if letter == 'X' else 'X'

        # If there are no more empty squares and no winner, it's a tie
        if game.num_empty_squares() == 0:
            if print_game:
                print("It's a tie!")
            return "Tie"

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
