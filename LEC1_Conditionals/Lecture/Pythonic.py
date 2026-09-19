"""
Parity Function: 짝수/홀수를 구별하는 함수

Pythonic Expression: 여러 줄을 간결하고 가독성 있게 한 줄로 표현할 수 있는 python만의 특징
    >>> return VALUE1 if CONDITION else VALUE2
"""

def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False  # Pythonic Expression
    #return (n % 2 == 0)
    
    
    """
    if n % 2 == 0:
        return True
    else:
        return False
  # boolean type: True / False, 첫 글자는 대문자로 입력
    """


main()