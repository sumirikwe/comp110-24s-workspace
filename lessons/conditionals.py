"""Demonstrate behavior of conditionals"""

user_input: str = input("pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if user_numer is even print "even"
if user_number % 2 == 0:
    print("even")

# if user_number is odd print "odd"
else: # user_number is odd
    print("odd")
    
print(user_input)