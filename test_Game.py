import unittest
from tic_tac_toe import Player
from tic_tac_toe import Game
import io
import sys


class TestGame(unittest.TestCase):
    def tearUp(self) -> None:
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("ai", "O", "hard")
        self.tic_tac_toe = Game(self.player1, self.player2)
        print("Inside tearUp()")
        print(self.tic_tac_toe)
        print(self.tic_tac_toe.print_board())

    def test_print_board(self):
        board = [[" " for _ in range(3)] for _ in range(3)]

        output = io.StringIO()
        sys.stdout = output
        self.tic_tac_toe.print_board()
        output_board = output.getvalue().strip() + "\n"
        sys.stdout = sys.__stdout__

        self.assertEqual(board, output_board)
