import random
import argparse


class Player:
    """Player Class for Tic Tac Toe Game"""

    def __init__(self, name: str, symbol: str, difficulty=None) -> None:
        self.name = name
        self.symbol = symbol
        self.difficulty = difficulty


class Game:
    """Game Class for Tic Tac Toe Game"""

    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        # self.current_player = random.choice([self.player1, self.player2])
        # self.opponent = (
        #     self.player2 if self.current_player == self.player1 else self.player1
        # )
        self.winner = None

    def print_board(self) -> None:
        """Prints the game board"""
        for row in self.board:
            print("|".join(row))

    def update_board(self, row: int, col: int, current_player: Player) -> None:
        """Updates the game board with the player's move"""
        self.board[row][col] = current_player.symbol

    def get_empty_spaces(self) -> list:
        """Returns a list of coordinates for all empty spaces on the board"""
        empty_spaces = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self.board[row][col] == " "
        ]

        return empty_spaces

    def is_win(self, player_symbol: str) -> bool:
        """Checks if the specified player has won the game"""
        # Check rows
        for row in self.board:
            if (
                row[0] == player_symbol
                and row[1] == player_symbol
                and row[2] == player_symbol
            ):
                return True

        # Check columns
        for i in range(3):
            if (
                self.board[0][i] == player_symbol
                and self.board[1][i] == player_symbol
                and self.board[2][i] == player_symbol
            ):
                return True

        # Check diagonals
        if (
            self.board[0][0] == player_symbol
            and self.board[1][1] == player_symbol
            and self.board[2][2] == player_symbol
        ):
            return True
        if (
            self.board[0][2] == player_symbol
            and self.board[1][1] == player_symbol
            and self.board[2][0] == player_symbol
        ):
            return True

        return False

    def get_move(self):
        """Gets the player's move and validates it"""

        while True:
            player_row = input("Enter row number (1-3): ")

            if not player_row.isdigit() or int(player_row) not in range(1, 4):
                print("Invalid row number, please try again.")
                continue
            else:
                player_row = int(player_row) - 1
                break

        while True:
            player_col = input("Enter column number (1-3): ")

            if not player_col.isdigit() or int(player_col) not in range(1, 4):
                print("Invalid column number, please try again.")
                continue
            else:
                player_col = int(player_col) - 1
                break

        return player_row, player_col

    def is_valid_move(self, row: int, col: int) -> bool:
        """Checks if the player's move is valid"""
        if self.board[row][col] != " ":
            return False

        return True

    def get_best_move(self, difficulty: str) -> tuple:
        """Uses the minimax algorithm to determine the best move for the AI player"""
        empty_spaces = self.get_empty_spaces()
        best_score = -float("inf")
        best_move = None

        for row, column in empty_spaces:
            self.board[row][column] = "O"
            score = self.minimax(self.board, 0, False)
            self.board[row][column] = " "

            if score > best_score:
                best_score = score
                best_move = (row, column)

        return best_move

    def minimax(self, board: list, depth: int, is_maximizing: bool):
        """Minimax algorithm for AI player"""
        # Base case: check if the game is over and return the score
        if self.is_win("O"):
            return 1
        elif self.is_win("X"):
            return -1
        empty_spaces = self.get_empty_spaces()
        if not empty_spaces:
            return 0

        # Recursive case: evaluate all possible moves and choose the best one
        if is_maximizing:
            best_score = -float("inf")
            for i, j in empty_spaces:
                board[i][j] = "O"
                score = self.minimax(self.board, depth + 1, False)
                board[i][j] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i, j in empty_spaces:
                board[i][j] = "X"
                score = self.minimax(self.board, depth + 1, True)
                board[i][j] = " "
                best_score = min(score, best_score)
            return best_score

    def play_game(self) -> None:
        """Tic Tac Toe game with AI or another player"""
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:

            # Player 1's turn
            self.player_turn(self.player1)

            # Player 2's turn
            if self.player2.name == "ai":
                self.ai_turn()

            else:
                self.player_turn(self.player2)

    def ai_turn(self) -> None:
        # Self.player2 is the AI player
        difficulty = self.player2.difficulty
        print("AI is thinking...")
        ai_row, ai_col = self.get_best_move(difficulty)
        self.update_board(ai_row, ai_col, self.player2)
        self.print_board()

        if self.is_win("O"):
            print("Sorry, you lose!")
            exit()

        if not self.get_empty_spaces():
            print("It's a tie!")
            exit()

    def evaluate(self):  # (self, board: list) -> int:
        """Evaluates the current state of the board from the perspective of the AI player"""
        # self.board
        if self.is_win("O"):
            return 1
        elif self.is_win("X"):
            return -1
        else:
            return 0

    def player_turn(self, player: Player):
        while True:
            player_row, player_col = self.get_move()

            if not self.is_valid_move(player_row, player_col):
                print("Space is already taken, please try again.")
                self.print_board()

            else:
                self.update_board(player_row, player_col, player)
                self.print_board()

                if self.is_win(player.symbol):
                    print(f"{player.name} Wins!")
                    exit()

                if not self.get_empty_spaces():
                    print("It's a tie!")
                    exit()

                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Tic Tac Toe", description="Tic Tac Toe game with AI or another player."
    )

    parser.add_argument(
        "-p",
        "--player",
        choices=["ai", "human"],
        default="ai",
        help="Play against the AI or another player.",
    )

    parser.add_argument(
        "-d",
        "--difficulty",
        choices=["easy", "hard"],
        default="hard",
        help="Difficulty level of the AI player.",
    )

    args = parser.parse_args()

    player1 = Player("Player 1", "X")
    player2 = Player(args.player, "O", args.difficulty)
    tic_tac_toe = Game(player1, player2)
    tic_tac_toe.play_game()
