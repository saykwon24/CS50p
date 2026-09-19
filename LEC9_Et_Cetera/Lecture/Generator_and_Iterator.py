"""
Generator: 함수를 generator로 정의하여 사용자에게 한 번에 막대한 양의 데이터를 생성하거나, 조금씩 생성할 수 있음
           메모리를 넘어서는 데이터를 한 번에 생성하면 프로그램이 제대로 동작하지 않음
           'yield' 키워드를 사용하면 (iterator를 반환하여) loop를 종료하지 않고 1개의 데이터씩 반환할 수 있음
           즉, one iteration and yield a result
    >>> https://docs.python.org/howto/functional.html#generators
"""


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i    # return a value at a time, and continue the loop


if __name__ == "__main__":
    main()