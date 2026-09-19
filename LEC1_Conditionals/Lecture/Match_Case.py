"""
match Statement: if, elif, else statement와 유사한 조건문, match 뒤에 오는 value와 case 뒤에 오는 value를 비교하여 True/False
                 case를 여러 가지로 두어 elif처럼 사용, 마지막 case 뒤에는 underscore(_)를 사용하여 else처럼 사용
                 or의 경우 '|'를 사용
"""

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":    # or == |
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
