"""
Type hint: 특정 변수의 type이 무엇인지에 관하여 Python에 힌트를 주는 것 (conventionally)
           type을 알려주는 일종의 comment같은 것
    >>> https://docs.python/org/3/library/typing.html

mypy: 코드가 type hint를 준수하는지 확인해주는 프로그램 'pip install mypy'
    >>> https://mypy.readthedocs.io


docstring: 주석의 다른 형태로, 3개의 따옴표를 사용하여 해당 코드의 기능을 설명하는 설명서의 역할을 함
           코드를 문서화하는 convention
"""


def meow(n: int) -> str:    # type hint 1: 'n' shoud be an integer
                            # type hint 2: 'meow' function returns a value of 'str' type
    # docstring
    """
    Meow n times.
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype(return type): str
    """
    return "meow\n" * n


number: int = int(input("Number: "))    # type hint: 'number' should be an integer
meows: str = meow(number)    # type hint: meows should be an string
print(meows, end="")