"""
Library: 다른 프로그램에서도 사용할 수 있도록(reusable) 한 code 'file'
Module:  하나 이상의 함수나 다른 기능이 내장된 library, 다른 프로그램에서 사용할 수 있음

import: module의 모든 기능에 접근할 수 있도록 하는 keyword
        module 내의 함수를 사용하고자 할 때에는 반드시 앞에 module name을 명시 (module.function())
from: module 내의 특정 함수를 불러오기 위한 keyword, 좀 더 구체적으로 지정하는 용도
      module의 특정 function이 namespace에 들어오게 되어, module 이름을 명시할 필요 없음 (function())
>>> module의 function 이름과 변수 등의 이름이 겹칠 수 있으므로, from보다는 import 키워드를 사용하는 것 권장 (상황에 따라 적절히 사용)


random module
    choice(seq): seq의 element를 같은 확률로 선택하여 return하는 함수
    randint(a, b): a 이상 b 이하의 정수를 같은 확률로 무작위 선택 후 return하는 함수
    shuffle(x): x의 element 순서를 무작위 재배치를 하는 함수, 특정 값을 반환하진 않음
"""


def main_1():
    import random    # import

    coin = random.choice(["heads", "tails"])    # choice()
    print(coin)


def main_2():
    from random import choice    # from

    coin = choice(["heads", "tails"])
    print(coin)


def main_3():
    import random

    number = random.randint(1, 10)    # randint()

    cards = ["jack", "queen", "king"]
    random.shuffle(cards)    # shuffle()
    for card in cards:
        print(card)


main_1()
main_2()
main_3()