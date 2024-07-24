import math
import random

# Base class for a player
class Player:
    def __init__(self, letter):
        self.letter = letter  # The letter can be 'X' or 'O'

    def get_move(self, game):
        pass  # This method will be overridden by subclasses


# Computer player that selects moves randomly
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Call the parent class constructor

    def get_move(self, game):
        # Get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


# Human player that inputs moves
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Call the parent class constructor

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')  # Changed to 0-8 for correct indexing

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError  # Raise an error if the move is not valid
                valid_square = True  # Exit the loop if a valid move is made
            except ValueError:
                print('Invalid square. Try again.')

        return val
    