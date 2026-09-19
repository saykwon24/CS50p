"""
==: 좌변과 우변이 같다는 의미
!=: 좌변과 우변이 같지 않다는 것을 의미
>: 좌변이 우변보다 큼
<: 좌변이 우변보다 작음
>=: 좌변이 우변보다 크거나 같음
<=: 좌변이 우변보다 작거나 같음

+, -, *, /: 사칙연산
%(modulo): 좌변을 우변으로 나눈 나머지를 반환

=: 우변을 좌변에 assignment
+=: 우변의 값을 좌변에 더한 값을 assignment
-=: 우변의 값을 좌변에서 뺀 값을 assignment
    python에는 ++, -- 없음
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")