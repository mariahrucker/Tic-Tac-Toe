from tic_tac_toe import Game
from tic_tac_toe import Player
import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.insert(0, os.path.abspath(".."))


def reset_board(board: list) -> None:
    """Reset the board to empty spaces"""
    for row in range(3):
        for col in range(3):
            board[row][col] = " "


class TestGame(unittest.TestCase):
    def tearUp(self) -> None:
        """Set up the test case"""
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("ai", "O", "hard")
        self.tic_tac_toe = Game(self.player1, self.player2)

    def test_print_board(self) -> None:
        """Test print_board() method"""
        self.tearUp()
        board = self.tic_tac_toe.board
        printed_board = ""
        for row in board:
            printed_board += "|".join(row) + "\n"

        # Captue the output of print_board()
        output = io.StringIO()
        sys.stdout = output
        self.tic_tac_toe.print_board()
        output_board = output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(printed_board, output_board)

    def test_update_board(self) -> None:
        """Test update_board() method"""
        self.tearUp()

        # Suppose it's player 1's turn
        self.tic_tac_toe.update_board(1, 1, self.player1)
        self.assertEqual(self.tic_tac_toe.board[1][1], "X")

        # Suppose it's player 2's turn
        self.tic_tac_toe.update_board(2, 2, self.player2)
        self.assertEqual(self.tic_tac_toe.board[2][2], "O")

    def test_get_empty_spaces(self) -> None:
        self.tearUp()

        self.tic_tac_toe.update_board(0, 0, self.player1)
        self.tic_tac_toe.update_board(1, 1, self.player2)
        self.tic_tac_toe.update_board(2, 2, self.player1)

        self.tic_tac_toe.print_board()

        # Get empty spaces from function
        empty_spaces = self.tic_tac_toe.get_empty_spaces()

        print(empty_spaces)

        # Get empty spaces from board manually
        empty_spaces_manually = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self.tic_tac_toe.board[row][col] == " "
        ]

        self.assertEqual(empty_spaces, empty_spaces_manually)

    def test_is_win(self) -> None:
        self.tearUp()

        # Check rows
        self.tic_tac_toe.update_board(0, 0, self.player1)
        self.tic_tac_toe.update_board(0, 1, self.player1)
        self.tic_tac_toe.update_board(0, 2, self.player1)

        self.tic_tac_toe.print_board()

        self.assertTrue(self.tic_tac_toe.is_win(self.player1.symbol))
        reset_board(self.tic_tac_toe.board)

        # Check columns
        self.tic_tac_toe.update_board(0, 1, self.player2)
        self.tic_tac_toe.update_board(1, 1, self.player2)
        self.tic_tac_toe.update_board(2, 1, self.player2)
        self.assertTrue(self.tic_tac_toe.is_win(self.player2.symbol))
        reset_board(self.tic_tac_toe.board)

        # Check diagonals
        self.tic_tac_toe.update_board(0, 0, self.player1)
        self.tic_tac_toe.update_board(1, 1, self.player1)
        self.tic_tac_toe.update_board(2, 2, self.player1)
        self.assertTrue(self.tic_tac_toe.is_win(self.player1.symbol))
        reset_board(self.tic_tac_toe.board)

        # Check diagonals
        self.tic_tac_toe.update_board(2, 0, self.player2)
        self.tic_tac_toe.update_board(1, 1, self.player2)
        self.tic_tac_toe.update_board(0, 2, self.player2)
        self.assertTrue(self.tic_tac_toe.is_win(self.player2.symbol))

    def test_get_move(self) -> None:
        pass

    def test_is_valid_move(self) -> None:
        self.tearUp()
        self.tic_tac_toe.update_board(0, 0, self.player1)

        # Mock input from player 2
        row, col = 0, 0

        self.assertFalse(self.tic_tac_toe.is_valid_move(row, col))

        # Mock input from player 2
        row, col = 2, 2
        self.assertTrue(self.tic_tac_toe.is_valid_move(row, col))
