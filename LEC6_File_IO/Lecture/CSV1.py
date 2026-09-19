"""
CSV(Comma-Seperated Values): 여러 유형의 값들을 comma로 구분하여 저장하는 text 파일의 한 종류
                             comma를 기준으로 column으로 구분하기 때문에, 스프레드시트, 엑셀 등과 연동하여 사용이 가능


dictionary 정렬 방법
1. 새로운 function 정의
    1) dictionary의 key에 대한 value를 반환하는 함수 f 정의
    2) sorted() 함수의 'key' argument에 함수의 이름 f'만' 전달 (python에서는 함수를 다른 함수의 argument로 전달 가능)
        >>> sorted(list of dicts, key=functionName, reverse=False)
    3) sorted() 함수가 list의 각 element인 dict에 대해 함수 f를 call
    4) 함수 f가 반환하는 값을 기준으로 list를 alphabetically 정렬

2. Lambda Function 사용
"""


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")      # .split()은 list를 반환하지만, 변수의 수를 맞추어 각각에 저장
        student = {"name": name, "house": house}    # dictionary 생성
        students.append(student)                    # list of dictionaries


def get_name(student):
    return student["name"]    # dictionary의 key에 해당하는 value 반환


for student in sorted(students, key=get_name):    # sorted() 함수가 get_name() 함수를 호출하는 것이므로, 함수의 이름만 전달
    print(f"{student['name']} is in {student['house']}")
