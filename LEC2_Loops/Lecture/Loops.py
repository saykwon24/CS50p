"""
while Loop: condition이 True이면 무한 반복하는 반복문   >>> while CONDITION:
            반복 횟수를 설정하기 위해서는 while loop 전에 iteration variable을 먼저 정의


for Loop: list의 element를 하나씩 pass하며 반복하는 반복문    >>> for i in LIST:
          변수 i를 해당 루프에서 사용하지 않는 경우, i 대신 underscore(_) 사용    >>> for _ in LIST:
          iteration variable을 사용하는 경우 반드시 명시
          range 함수를 사용해서 반복 횟수 설정 가능

range(n): 0 ~ n-1의 정수(n개의 정수) list를 반환하는 함수


continue: 즉시 가장 가까운 loop의 다음 cycle 실행하는 keyword
break: 즉시 가장 가까운 loop를 탈출하는 keyword
       반면 return은 loop에 관계 없이 즉시 함수를 종료하는 keyword
"""


# while Loop
i = 0
while i < 3:
    print("meow")
    i += 1


# for Loop
for _ in range(3):
    print("meow")

print("meow\n" * 3, end="")    # pythonic expression


# Using Function
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break    # 가장 '가까운' while loop 탈출
    
    return n    # function exit


def meow(n):
    for _ in range(n):
        print("meow")


main()