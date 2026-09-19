"""
Operator Overloading: 하나의 연산자가 data type에 따라 여러 역할을 수행하는 것을 의미
                      예를 들어, +의 경우 숫자 덧셈, 문자열 연결 등 다양한 역할을 수행
                      overload할 수 있는 연산자는 정해져 있음
    >>> https://docs.python.org/3/reference/datamodel.html#special-method-names

object.__add__(self, other): '+' 연산자를 기준으로 왼쪽에 있는 것은 self, 오른쪽은 other로 받는 instance method
                             왼쪽에 있는 class 내에 __add__ method가 구현되어 있다면, 오른쪽에 오는 것은 어떤 type이든 상관 없음
"""


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    # defind '+' operator's behavior (overload)
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley    # plus two classes -> overloaded operator '+'
print(total)