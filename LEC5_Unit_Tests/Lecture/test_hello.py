from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"
    # hello() 함수에서 print() 함수로 출력하는 경우, 값을 return하는 것이 아닌 단지 side effect(눈에 보이는 형태)이므로 error 발생 가능
    # 따라서 test 시에는 가능하다면 side effect를 발생시키지 않도록 하는 것이 베스트
