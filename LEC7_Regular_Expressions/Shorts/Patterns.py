"""
Hexadecimal Color Code '#RRGGBB'
    R == red, G == green, B == blue
    R, G, B는 00~FF의 값을 가지고, FF가 가장 큰 값이며, 이는 각 색의 shade를 나타냄
"""


import re


def main():
    code = input("Hexadecimal code: ").strip()
    
    pattern = r"^#[a-fA-F0-9]{6}$"
    if match := re.search(pattern, code):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")


main()