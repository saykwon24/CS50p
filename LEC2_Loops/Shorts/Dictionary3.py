"""
Dictionary Methods (3)
    .itmes():  dict의 key-value pair를 가져오는 method
    .clear():  dict의 모든 key를 remove하는 method
    .pop(key): dict의 key를 remove, 대응되는 value를 pop하는 method
"""


WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main_1():
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


def main_2():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")
        
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
        
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
    
    print("That's the game!")


main_1()
main_2()