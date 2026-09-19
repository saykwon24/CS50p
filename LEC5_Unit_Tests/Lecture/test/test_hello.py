# 'pytest folderName': pytest가 자동으로 폴더를 검색하여 그 내부에 있는 가능한 모든 test를 찾아 실행

from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"