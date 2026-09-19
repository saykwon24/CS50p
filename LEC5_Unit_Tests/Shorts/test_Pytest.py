import pytest
from Pytest import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_error():
    with pytest.raises(TypeError):    # expect TypeError
        convert("1")


# floating point precision: 숫자를 표현할 때 항상 유한한 수의 비트가 사용되므로, float value는 정확하지 않을 수 있음
# 따라서 float를 test할 때에는 허용 오차를 두어 테스트
def test_float_conversion():
    # pytest.approx(num, err): 'num +- err'의 범위에 있으면 같다고 판단
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)    # (base)e(power) == base * 10^(power)
        # 허용 오차를 먼저 정한 후, 우리가 기대하는 값을 반환하는지 확인