"""Practice with variables and input function."""

first_name: str = input("what is your name?")

fav_number_str: str = input("what is your favorite number?")

fav_number: int = int(fav_number_str)

higher_number: int = fav_number + 1

print("Hello " + first_name + "!")
print("my favorite number is " + str(higher_number))

