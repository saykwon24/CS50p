"""
Boolean: True/False의 2가지 값을 갖는 data type


if Statement: condition이 True이면 해당 조건문 실행
elif Statement: if가 아닌 다른 condition, True이면 해당 조건문 실행
else Statement: if, elif가 아닌 여집합의 condition, if와 elif가 모두 False이면 실행


or: 좌변 또는 우변이 True이면 True 반환
and: 좌변과 우변 모두 True일 때에만 True 반환
not: 우측의 조건이 True(False)이면 False(True) 반환
"""

score = int(input("Score: "))

if 90 <= score <= 100:    # score >= 90 and score <= 100
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
