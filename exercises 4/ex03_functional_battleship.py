"""Functional Battleship"""

__author__ = "730477259"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
secret_row: int = 2
secret_column: int = 1

def input_guess(grid_size: int, row_col: str) -> int:
    assert row_col == "row" or row_col == "column"
    if row_col == "row":
        guess_row: int = int(input("Guess a row: "))

        while guess_row < 1 or guess_row > grid_size:
            try_1: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            
            if try_1 >= 1 and try_1 <= grid_size:
                guess_row = try_1
        
        return guess_row  # Return the guess
    elif row_col == "column":
        guess_column: int = int(input("Guess a column: "))
        
        while guess_column < 1 or guess_column > grid_size:
            try_2: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            
            if try_2 >= 1 and try_2 <= grid_size:
                guess_column = try_2
        
        return guess_column  # Return the guess


def print_grid(grid_size: int, guess_row: int, guess_column: int, user_guess: bool) -> None:
    result_box: str = ""

    if user_guess:  # Check if it's a user's guess
        result_box = RED_BOX  # Red box for user's guess
    else:
        result_box = WHITE_BOX  # White box for missed guess

    row_counter: int = 1

    while row_counter <= grid_size:
        row_str: str = ""
        column_counter: int = 1
        
        if row_counter == guess_row: 
            while column_counter <= grid_size:
                if column_counter == guess_column:
                    row_str += result_box
                else:
                    row_str += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid_size:
                row_str += BLUE_BOX
                column_counter += 1
        print(row_str)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    if secret_row == guess_row and secret_column == guess_column:
        print("True")
        return True
    else:
        print("False")
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    # Variables to keep track of game state
    turn: int = 1
    game_won: bool = False

    # Game loop
    while turn <= 5 and not game_won:
        print(f"=== Turn {turn}/5 ===")

        # Prompt user for guess
        guess_row = input_guess(grid_size, "row")
        guess_column = input_guess(grid_size, "column")
        correct_guess(secret_row, secret_column, guess_row, guess_column)

        # Verify guess
        if secret_row == guess_row and secret_column == guess_column:
            print_grid(grid_size, guess_row, guess_column, True)
            print(f"Hit! You won in, {turn}/5 turns!")
            game_won = True
        else:
            print_grid(grid_size, guess_row, guess_column, False)
            print("Miss!")
            turn += 1

    # If all turns are exhausted and the game is not won
    if turn >= 6:
        print("X/5 - Better luck next time!")

main(4, 4, 4)