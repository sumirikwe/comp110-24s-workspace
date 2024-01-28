"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730477259"

Location1_str: str = input("Pick a secret boat location between 1 and 4: ")

Location1: int = int(Location1_str)

if Location1 == 1-4:
    print("")

else:
   if Location1 == 0:
       print("Error! 0 too low!"), exit()
if Location1 >= 5:
           print("Error! # too high!"), exit()

Guess_ship_str: str = input("Guess a number between 1 and 4: ")

Guess_ship: int = int(Guess_ship_str)

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if Guess_ship == 1-4:
    print("")

else:
   if Guess_ship == 0:
       print("Error! 0 too low!"), exit()
if Guess_ship >= 5:
           print("Error! # too high!"), exit()


if  Location1 == 1 and Guess_ship == 1:
      print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
else:
      if Guess_ship == 1 and Location1 != Guess_ship:
            print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)

if  Location1 == 2 and Guess_ship == 2:
      print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
else:
      if Guess_ship == 2 and Location1 != Guess_ship:
            print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)

if  Location1 == 3 and Guess_ship == 3:
      print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
else:
      if Guess_ship == 3 and Location1 != Guess_ship:
            print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)

if  Location1 == 4 and Guess_ship == 4:
      print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
else:
      if Guess_ship == 4 and Location1 != Guess_ship:
            print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)


if Location1 != Guess_ship:
      print("Incorrect! You missed the ship.")
else:
      print("Correct! You hit the ship.")


      