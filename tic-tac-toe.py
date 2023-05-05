import random
import argparse

# Add a multiplayer to the code with difficulty level


def play_game_difficulty(difficulty_level) -> None:
    """Tic Tac Toe game with difficulty level"""

    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    turn = 0

    while True:
        if turn % 2 == 0:
            player1_row, player1_col = get_move()

            if board[player1_row][player1_col] == " ":
                board[player1_row][player1_col] = "X"
                print_board(board)

                if is_win(board, "X"):
                    print("Congratulations, Player 1 wins!")
                    return

                if not get_empty_spaces(board):
                    print("It's a tie!")
                    return
            else:
                print("That space is already taken, please try again.")
        # else:
        #    if difficulty_level == "easy":


def print_board(board: list) -> None:
    """Prints the game board"""
    for row in board:
        print("|".join(row))


def update_board(board: list, row: int, col: int, player: str) -> None:
    """Updates the game board with the player's move"""
    board[row][col] = player


def get_empty_spaces(board: list) -> list:
    """Returns a list of coordinates for all empty spaces on the board"""
    empty_spaces = [
        (row, col) for row in range(3) for col in range(3) if board[row][col] == " "
    ]

    return empty_spaces


def is_win(board: list, player: str) -> bool:
    """Checks if the specified player has won the game"""
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def evaluate(board: list):
    """Evaluates the current state of the board from the perspective of the AI player"""
    if is_win(board, "O"):
        return 1
    elif is_win(board, "X"):
        return -1
    else:
        return 0


def minimax(board: list, depth: int, is_maximizing: bool):
    """Minimax algorithm for AI player"""
    # Base case: check if the game is over and return the score
    if is_win(board, "O"):
        return 1
    elif is_win(board, "X"):
        return -1
    empty_spaces = get_empty_spaces(board)
    if not empty_spaces:
        return 0

    # Recursive case: evaluate all possible moves and choose the best one
    if is_maximizing:
        best_score = -float("inf")
        for i, j in empty_spaces:
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in empty_spaces:
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score


def get_best_move(board: list) -> tuple:
    """Uses the minimax algorithm to determine the best move for the AI player"""
    empty_spaces = get_empty_spaces(board)
    best_score = -float("inf")
    best_move = None

    for row, column in empty_spaces:
        board[row][column] = "O"
        score = minimax(board, 0, False)
        board[row][column] = " "

        if score > best_score:
            best_score = score
            best_move = (row, column)

    return best_move


def get_move():
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


def is_valid_move(board: list, row: int, col: int) -> bool:
    """Checks if the player's move is valid"""
    if board[row][col] != " ":
        return False

    return True


# Main Game Loop
def play_game() -> None:
    """Tic Tac Toe game with AI"""
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_row, player_col = get_move()

        if is_valid_move(board, player_row, player_col):
            update_board(board, player_row, player_col, "X")
            print_board(board)

            if is_win(board, "X"):
                print("Congratulations, you win!")
                break

            if not get_empty_spaces(board):
                print("It's a tie!")
                break

            print("AI is thinking...")
            ai_row, ai_col = get_best_move(board)

            update_board(board, ai_row, ai_col, "O")
            print_board(board)

            if is_win(board, "O"):
                print("Sorry, you lose!")
                break

            if not get_empty_spaces(board):
                print("It's a tie!")
                break
        else:
            print("Space is already taken, please try again.")
            print_board(board)


if __name__ == "__main__":
    play_game()
