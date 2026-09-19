"""
Unpacking: string, list 등을 여러 개의 변수에 할당하여 분해하는 것을 의미
           list, tuple의 원소를 함수의 인수로 unpack하여 전달하고자 할 때에는 '*'(*args), dict는 '**'(**kwargs) 사용
           이때 함수의 인수 개수와 원소의 개수가 같아야 하고, dict의 경우 key와 함수 인수의 이름이 같아야 함

*args, **kwargs: unpacking뿐만 아니라 visual indicator로도 사용
                 예를 들어, 함수에서 가변적인 개수의 인수를 취하는 것으로 사용되어 여러 개의 변수가 올 수 있음
                 *args, **kwargs 순으로 위치해야 하고, args와 kwargs는 다른 이름으로 지정 가능
    *args: 'positional' argument, return as tuple
    **kwargs: 'named' argument, return as dict
"""


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# Using list
coins = [100, 50, 25]
print(total(*coins), "Knuts")    # unpack the list by '*'

# Using dict
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts")    # unpack the dict by '**'
                                  # unpack into the form 'key=value'
                                  # so keys should be same as function's arg names


# Positional(*args) and Named(**kwargs) arguments
def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

f(100, 50, 25)    # positional
f(galleons=100, sickles=50, knuts=25)    # named
