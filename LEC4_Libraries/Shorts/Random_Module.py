"""
Random Module
    random.choice(list): list에서 무작위로 하나의 element를 선택
    random.choices(list, weights=[], k=n): list에서 무작위로 n개의 element를 선택 (중복 허용)
                                           weights는 각 element의 선택 확률을 지정하는 list of floats(0~1) or ints(0~100)
    random.sample(list, k=n): list에서 무작위로 n개의 element를 선택 (중복 불허)
    random.seed(x): random 모듈의 난수 생성기를 초기화
                    특정 seed 값인 x를 넣으면, 동일한 난수 sequence를 생성 -> debugging에 유용
"""


import random

cards = ["jack", "queen", "king", "ace"]


def main():
    print(random.choice(cards))
    
    print(random.choices(cards, k=2))    # sampling with replacement
    print(random.choices(cards, weights=[60, 30, 10], k=2))
    
    print(random.sample(cards, k=2))     # sampling without replacement
    
    random.seed(0)
    print(random.choices(cards, k=2))


main()