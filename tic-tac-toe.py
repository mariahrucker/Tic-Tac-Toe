import random

# Add a multiplayer to the code with difficulty level 
def play_game(difficulty_level):
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    turn = 0
    while True:
        if turn % 2 == 0:
            player1_row = int(input("Player 1 - Enter row number (1-3): ")) - 1
            player1_col = int(input("Player 1 - Enter column number (1-3): ")) - 1
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
        else:
            if difficulty_level == "easy":

# Prints the game board
def print_board(board):
    for i in range(3):
        print("|".join(board[i]))

# Returns a list of coordinates for all empty spaces on the board
def get_empty_spaces(board):
    empty_spaces = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_spaces.append((i, j))
    return empty_spaces

# Checks if the specified player has won the game
def is_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
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

# Evaluates the current state of the board from the perspective of the AI player
def evaluate(board):
    if is_win(board, "O"):
        return 1
    elif is_win(board, "X"):
        return -1
    else:
        return 0

# Recursive function that implements the minimax algorithm
def minimax(board, depth, is_maximizing):
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
            score = minimax(board, depth+1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in empty_spaces:
            board[i][j] = "X"
            score = minimax(board, depth+1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

# Uses the minimax algorithm to determine the best move for the AI player
def get_best_move(board):
    empty_spaces = get_empty_spaces(board)
    best_score = -float("inf")
    best_move = None
    for i, j in empty_spaces:
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        player_row = int(input("Enter row number (1-3): ")) - 1
        player_col = int(input("Enter column number (1-3): ")) - 1
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "X"
            print_board(board)
            if is_win(board, "X"):
                print("Congratulations, you win!")
                return
            if not get_empty_spaces(board):
                print("It's a tie!")
                return
            print("AI is thinking...")
            ai_row, ai_col = get_best_move(board)

            board[ai_row][ai_col] = "O"
            print_board(board)
            if is_win(board, "O"):
                print("Sorry, you lose!")
                return
            if not get_empty_spaces(board):
                print("It's a tie!")
                return
        else:
            print("That space is already taken, please try again.")

play_game()
