def test_play_game():
    # Test the case where the player wins
    input_values = [
        "1", "1", # Player move
        "2", "2", # Player move
        "1", "2", # Player move
        "3", "3", # Player move
    ]
    output = []
    def mock_input():
        return input_values.pop(0)
    def mock_print(s):
        output.append(s)
    # Replace input and print functions
    __builtins__.input = mock_input
    __builtins__.print = mock_print
    # Play the game
    play_game()
    # Check if the game output is correct
    assert "Congratulations, you win!" in output

    # Test the case where the game is a tie
    input_values = [
        "1", "1", # Player move
        "2", "2", # Player move
        "3", "1", # Player move
        "2", "1", # Player move
        "2", "3", # Player move
        "1", "2", # Player move
        "3", "2", # Player move
        "1", "3", # Player move
        "3", "3", # Player move
    ]
    output = []
    # Replace input and print functions
    __builtins__.input = mock_input
    __builtins__.print = mock_print
    # Play the game
    play_game()
    # Check if the game output is correct
    assert "It's a tie!" in output

    # Test the case where the AI wins
    input_values = [
        "1", "1", # Player move
        "2", "2", # Player move
        "1", "2", # Player move
        "2", "1", # Player move
        "3", "3", # Player move
    ]
    output = []
    # Replace input and print functions
    __builtins__.input = mock_input
    __builtins__.print = mock_print
    # Play the game
    play_game()
    # Check if the game output is correct
    assert "Sorry, you lose!" in output
