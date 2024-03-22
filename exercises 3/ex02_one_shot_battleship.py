"""One Shot Battleship."""

__author__ = "730477259"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row: int = int(input("Guess a row: "))

while guess_row < 1 or guess_row > grid_size:
   try_1: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

   if try_1 >= 1 and try_1 <= grid_size:
      guess_row = try_1

guess_column: int = int(input("Guess a column: "))

while guess_column < 1 or guess_column > grid_size:
   try_2: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

   if try_2 >= 1 and try_1 <= grid_size:
      guess_column = try_2

result_box: str = ""

if guess_row == secret_row and guess_column == secret_column:
    result = RED_BOX
else:
   guess_row == secret_row or guess_column == secret_column
   result = WHITE_BOX


row_counter: int = 1

while row_counter <= grid_size:
   row_str: str = ""
   column_counter: int = 1

   if row_counter == guess_row: 
      while column_counter <= grid_size:
         if column_counter == guess_column:
            row_str += result
         else:
            row_str += BLUE_BOX
         column_counter += 1
   else:
      while column_counter <= grid_size:
         row_str += BLUE_BOX
         column_counter += 1
   print(row_str)
   row_counter += 1

if guess_row == secret_row and guess_column == secret_column:
   print("Hit!")
elif guess_row == secret_row:
   print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
   print("Close! Correct column, wrong row.")
else:
   print("Miss!")