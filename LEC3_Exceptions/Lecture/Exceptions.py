"""
Error: 다양한 종류의 error가 있고 언제 어디서 나타날지 모르기 때문에, 'defensively'하게 coding
    SyntaxError: unterminated, 시작을 했지만 종료가 되지 않은 경우를 의미
    ValueError: invalid literal, 잘못된 type을 의미
    NameError: 변수의 이름으로 잘못된 작업을 하는 경우


try-except, else Exceptions: try statement에서 error가 발생하지 않으면 else statement 실행, 발생하면 except statement 실행
                             오직 error가 날 수 있는 부분'만' try에 넣으면 되므로, 정상적으로 동작하는 부분은 else로 따로 빼서 작성
                             따라서 code의 어느 부분에서 error가 발생할 수 있는지 프로그래머가 알아야 하고, 어떤 종류의 error인지도 파악을 해야 함
"""


def main():
    x = get_int("What's x? ")    # main()과 get_int()가 같은 변수 x를 공유할 필요는 없으므로, get_int() 함수에 parameter를 추가하여 reusable하게 만듦
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #print("x is not a integer")
            pass


main()