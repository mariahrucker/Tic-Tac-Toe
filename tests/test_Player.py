import unittest
from tic_tac_toe import Player
import sys
import os

sys.path.insert(0, os.path.abspath(".."))


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "X", None)
        self.player2 = Player("ai", "O", "hard")

    def test_player(self):
        """Test Player class"""
        assert self.player1.name == "Player 1"
        assert self.player1.symbol == "X"
        assert self.player1.difficulty == None
        assert self.player2.name == "ai"
        assert self.player2.symbol == "O"
        assert self.player2.difficulty == "hard"
