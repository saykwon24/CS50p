"""
string의 일부만을 추출하고자 하는 경우, re.search() 함수의 'pattern' argument에 parenthesis를 이용
반대로 추출에서 제외하고자 하는 경우, non-capturing version([?:...])을 이용

re.search() 함수는 'pattern' argument의 모든 괄호 group을 반환
    index 0에는 string과 관련된 다른 값이 저장되어 있어, 여러 괄호 group이 존재하는 경우 앞에서부터 group 1, 2, ... 순으로 index 지정
    .groups(): 괄호 group들을 모두 반환하는 method
    .group(n): 괄호 group들을 담고 있는 변수에서 n번째 group을 반환하는 method


Walrus Operator(:=): 우변을 좌변에 할당하고, 동시에 같은 줄에 if나 elif의 Boolean question을 판별하고자 할 때 사용
"""


import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):    # Walrus Operator
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")