"""
global variable은 하나의 프로그램 전체에서 사용할 수 있지만, 특정 함수 등의 영역 내에서는 read-only (write 불가능)
하나의 함수 내에 변수를 정의하면 해당 함수 내에서만 접근할 수 있는 local variable이므로, 다른 함수에서는 접근 불가능
전역 변수를 다른 함수의 argument로 지정하더라도 copy의 값을 변경하므로, 실질적으로 원본의 값은 그대로 유지됨

global: 함수 A의 (지역) 변수를 다른 함수 B에서도 사용할 수 있도록 전역 변수로 설정하는 keyword
        함수 B에서 global keyword를 사용하여 해당 함수에서 사용할 것임을 알림

전역 변수를 많이 쓰게 되면 프로그램이 복잡해질수록 해당 정보가 어디에 있는지 unclear하게 되므로,
일반적으로는 전역 변수를 적게 쓰되, OOP의 특징을 살려 class 내에서 instance variable을 사용하여 self로 해당 변수를 접근하도록 프로그래밍
"""


balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()



"""
class Account:
    def __init__(self):
        self._balance = 0    # '_' is visual clue indicating it is 'private'
                             # prevent colliding with property

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
"""