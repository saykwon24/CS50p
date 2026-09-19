"""
Functional programming: side effect, printing 또는 changing of state가 global하게 없음
                        input과 return value를 취하는 완전히 self-contained인 형태

map(function, iterable, ...): some function과 every element of some sequence를 mapping하는 함수
"""


def main():
    yell("This", "is", "cs50")


def yell(*words):
    uppercased = map(str.upper, words)    # just pass upper method to map's argument, not call
                                          # return a list whose elements are uppercased
                                          # upper method  doen't need '()' when is used as an argument
    # List Comprehension
    uppercased = [word.upper() for word in words]
    
    print(*uppercased)


if __name__ == "__main__":
    main()