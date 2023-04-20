Implementation of Tic Tac Toe game in Python. 
It includes a game board, player moves, win detection, and an AI opponent using the minimax algorithm.

```python
import random

def print_board(board):
    for i in range(3):
        print("|".join(board[i]))

def get_empty_spaces(board):
    empty_spaces = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_spaces.append((i, j))
    return empty_spaces

def is_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def evaluate(board):
    if is_win(board, "O"):
        return 1
    elif is_win(board, "X"):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if is_win(board, "O"):
        return 1
    elif is_win(board, "X"):
        return -1
    empty_spaces = get_empty_spaces(board)
    if not empty_spaces:
        return 0
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
```

Explanation:

1. `print_board()` function prints the game board on the console.
2. `get_empty_spaces()` function returns a list of empty spaces on the board.
3. `is_win()` function checks if a player has won the game.
4. `evaluate()` function evaluates the board and returns a score for the AI's move.
5. `minimax()` function implements the minimax algorithm for the AI's move.
6. `get_best_move()` function returns the best move for the AI to make based on the current board.
7. `play_game()` function initiates and plays the game.

The game board is represented by a 2D list of 3x3 size, where "X" represents the player's move, "O" represents the AI's move, and " " (empty string) represents an empty space on the board.

In the `play_game()` function, the player enters their move by specifying the row and column number of the board. The function checks if the move is valid, i.e., if the space is empty, and adds the move to the board if it is valid. It then checks if the player has won the game or if the game is tied. If the game is still ongoing, the AI calculates its best move using the `get_best_move()` function and adds it to the board. It then checks if the AI has won the game or if the game is tied. If the game is still ongoing, the process continues until the game is over.

The AI opponent uses the minimax algorithm to calculate the best move. This algorithm recursively explores all possible moves to a certain depth and returns the score for each move. The score is evaluated using the `evaluate()` function. The AI opponent chooses the move with the highest score.

Overall, this implementation of Tic Tac Toe game in Python is quite complex and involves multiple functions and algorithms. It provides a good example of how to use the minimax algorithm in a game-playing AI.
