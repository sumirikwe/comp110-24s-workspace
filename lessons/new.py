"""Odd and even!"""

def odd_and_even(x: list[int]) -> list[int]:
    index: int = 0
    list_2: list[int] = []
    while index < len(x):
        if x[index] % 2 == 1:
            list_2.append(x[index])
        index += 1
    print(list_2)
    return list_2

a: list[int] = [6 , 8 , 10 , 7 , 5 , 12 , 3 , 2 , 11 , 8]

odd_and_even(a)

def short_words(abc:list[str]) -> list[str]:
    """Returns a lists of words!"""
    index: int = 0
    list_2: list[str]= []
    while index < len(abc):
        if len(abc[index]) < 5:
            list_2.append(abc[index])
        else:
            print(f"{abc[index]} is too long")
        index += 1
    print(list_2)
    return list_2
    
my_list : list [str ] = ["sun", "cloud", "sky", "Hello", "dab"]
short_words(my_list)