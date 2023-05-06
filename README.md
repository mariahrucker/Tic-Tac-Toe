# Tic Tac Toe Game

In this Python implementation of the classic game Tic Tac Toe, players and an AI opponent take turns placing their moves on a 3x3 board. The first player to make three consecutive marks in a row wins the game.

## Functions

### `print_board()`

Prints the current state of the game board on the console.

### `get_empty_spaces()`

Returns a list of empty spaces on the board.

### `is_win()`

Checks if a player has won the game.

### `evaluate()`

Evaluates the board and returns a score for the AI's move.

### `minimax()`

Implements the minimax algorithm for the AI's move.

### `get_best_move()`

Returns the best move for the AI to make based on the current board.

### `play_game()`

Initiates and plays the game. The player enters their move by specifying the row and column number of the board. The function checks if the move is valid and adds it to the board if it is valid. It then checks if the player has won the game or if the game is tied. If the game is still ongoing, the AI calculates its best move using the `get_best_move()` function and adds it to the board. It then checks if the AI has won the game or if the game is tied. If the game is still ongoing, the process continues until the game is over.

## Board Representation

The game board is represented by a 2D list of 3x3 size, where "X" represents the player's move, "O" represents the AI's move, and " " (empty string) represents an empty space on the board.

## AI opponent

The AI opponent uses the minimax algorithm to calculate the best move. This algorithm recursively explores all possible moves to a certain depth and returns the score for each move. The score is evaluated using the `evaluate()` function. The AI opponent chooses the move with the highest score.

## How to Play

To play the game, run the `play_game()` function in a Python environment.

## Example

Here's an example of a game being played:

```
     |     |
  X  |     |  O
_____|_____|_____
     |     |
     |  X  |
_____|_____|_____
     |     |
  O  |     |
     |     |
```

In this example, the player (represented by "X") has made the first move in the top-left corner. The AI opponent (represented by "O") has made the second move in the center. The player has made the third move in the center-left. The game is still ongoing.

## Requirements

Implementation of Tic Tac Toe requires Python 3.x.

## Installation

To use this implementation of Tic Tac Toe, simply clone the repository and import the functions into your Python environment.

## License

Implementation of Tic Tac Toe is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions to this implementation of Tic Tac Toe are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or pull request on the GitHub repository.

## Credits

Implementation of Tic Tac Toe was created by Mariah Rucker.

## Contact

If you have any questions or concerns, please feel free to contact Mariah Rucker at mariahrucker@myyahoo.com.

## Conclusion

Python implementation of Tic Tac Toe is a fun and simple game that can be played on the console. It uses the minimax algorithm to provide a challenging opponent for the player. Try it out and see if you can beat the AI!
