"""Demonstrate Basic List Syntax!"""

# Initialize an empty list
grocery_list: list[str] = list() #This is what creates the list
grocery_list: list[str] = [] # <- literal

print(grocery_list)

#add items to a list

grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("cereal")

print("After appending: ")
print(grocery_list)

#create an already populated list
new_grocery_list: list[str] = ["bananas", "milk", "cereal"]

print(new_grocery_list)

new_grocery_list.append("eggs")

print(new_grocery_list)

print("Print first item in list")
print(new_grocery_list[0])

#modify item in list
new_grocery_list[1] = "almond milk"
print(new_grocery_list)

new_grocery_list.append("almond milk")

print(new_grocery_list)

new_grocery_list[2] = "low fat cereal"

print(new_grocery_list)

print(len(grocery_list))
print(len(new_grocery_list))

# to remove an item from list
new_grocery_list.pop(4)


display: list[str] = ["tv", "monitor", "movie", "screen"]
display.append("")

print(len(display))
print(display[len(display) - 1])

def create(string1: str, string2: str) -> list[str]:
    name: list[str] = [string1, string2]
    return name
    
print(create("hello", "world"))