"""
Unit Test: 일반적으로 사용자가 작성한 function에 대한 테스트를 의미, function 단위로 테스트
           test code가 복잡해지면 그 자체도 또다시 test를 해야 할 수 있으므로, 깔끔하고 간단하게 작성
           test 함수를 여러 개로 나누어 pytest를 실행하면 각 함수에 대해 test하므로, error에 대한 단서를 다양하게 얻을 수 있음

assert: 뒤에 오는 statement가 True여야 한다고 주장(assert)하는 keyword
        해당 statement가 False이면 AssertionError 발생, 이는 error가 발생한 line만 알려줌


pytest: code를 test하는 프로그램, third-party library (package)
        pytest에서는 test code를 담은 파일은 'test_'로 시작하는 것이 관례, test code 파일에 사용하는 함수들도 마찬가지로 'test_'로 시작
        command-line에 'pytest'를 입력하면 'test_'로 시작하는 파일을 모두 테스트
>>> 'pytest fileName.py' or 'pytest'

pytest.raises(ERROR): 아래의 statement를 실행했을 때 발생할 error의 종류를 명시하여 예외 발생을 예상한다는 의미
"""


from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0


import pytest

def test_str():
    with pytest.raises(TypeError):
        square("cat")