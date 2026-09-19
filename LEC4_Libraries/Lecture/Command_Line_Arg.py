"""
command-line arguments: commad line에 입력한 것이 실행할 프로그램의 argument로 입력되는 것, '입력 인수'

sys module: command line에 입력한 값에 접근할 수 있도록 하는 module
    sys.argv: command line에 입력한 것들을 element로 갖는 'list' (argument vector)
              공백으로 구분하여 저장, 하나의 element로 입력하려면 ""로 묶어서 입력
              1번째 원소인 sys.argv[0]에는 실행하려는 파일 이름이 저장
    sys.exit("str"): error 발생 시 str를 출력한 후 해당 프로그램을 종료
"""


import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:    # 1 ~ n-1번째 element를 slicing
    print("hello, my name is", arg)
