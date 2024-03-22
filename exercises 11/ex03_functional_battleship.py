"""Functional Battleship."""

__author__ = "730477259"

import random


def input_guess(grid_size: int, row_col: str) -> int:
    """Inputs guess row or column."""
    assert row_col == "row" or row_col == "column"
    if row_col == "row":
        guess_row: int = int(input("Guess a row: "))

        while guess_row < 1 or guess_row > grid_size:
            try_1: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            
            if try_1 >= 1 and try_1 <= grid_size:
                guess_row = try_1
        
        return guess_row
    elif row_col == "column":
        guess_column: int = int(input("Guess a column: "))
        
        while guess_column < 1 or guess_column > grid_size:
            try_2: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            
            if try_2 >= 1 and try_2 <= grid_size:
                guess_column = try_2
        
        return guess_column


def print_grid(grid_size: int, guess_row: int, guess_column: int, user_guess: bool) -> None:
    """Print the battlefield grid.""" 
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str = ""

    if user_guess:
        result_box = RED_BOX  
    else:
        result_box = WHITE_BOX 

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
    """Track the correct guess."""
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """This the main battlefield function."""
    turn: int = 1
    game_won: bool = False

    while turn <= 5 and not game_won:
        print(f"=== Turn {turn}/5 ===")

        guess_row = input_guess(grid_size, "row")
        guess_column = input_guess(grid_size, "column")

        if correct_guess(secret_row, secret_column, guess_row, guess_column):
            print_grid(grid_size, guess_row, guess_column, True)
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            game_won = True
        else:
            print_grid(grid_size, guess_row, guess_column, False)
            print("Miss!")
            turn += 1
    if turn >= 6:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
