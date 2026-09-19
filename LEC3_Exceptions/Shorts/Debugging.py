"""
Debugging 방법
1) print()는 변수 등의 값을 확인하여 디버깅을 하는 가장 기본적이면서 효과적인 방법
2) breakpoints: 좌측 번호 왼쪽에 나타나는 빨간 동그라미 -> Ctrl + Shift + D / 좌측 패널의 'Run and Debug' 클릭
"""


def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):    # i = 0, 1, 2, ..., n
        print("#" * i)    # debug this line


if __name__ == "__main__":
    main()