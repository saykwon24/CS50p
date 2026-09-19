"""
csv.reader(csvfile): csvfile을 한 줄씩 읽어들이고, comma를 기준으로 나누어 row 별로 list를 생성한 후, 이러한 list의 집합을 갖는 reader object를 반환
                     >>> 2차원 list (list of lists): [[~], [~], ..., [~]]

1) 각 row가 list로 표현되어 있으면 row 별로 봤을 때 element가 어떤 항목을 가리키고 있는지 판단하기 어려움
2) csv 파일의 column의 순서가 바뀌거나 새로 추가되면 원하는 결과를 얻지 못할 수 있음
>>> 이러한 문제를 해결하기 위해 각 row를 dictionary로 표현하는 방법을 주로 사용

csv.DictReader(f, fieldnames=None): fieldnames에 주어진 list의 element를 key로, f를 한 줄씩 읽어들여 comma를 기준으로 나눈 str을 value로 하는 dictionary의 집합을 갖는 object를 반환
                                    fieldnames가 주어지지 않으면, csv 파일 첫 줄의 header를 dictionary의 key로 사용한 후 나머지 부분을 object로 반환
                                    header의 수 or fieldnames의 수가 comma를 기준으로 나뉘는 string의 수와 같아야 함
                                    >>> list of dicts: [{~}, {~}, ..., {~}]


reader와 DictReader는 comma를 기준으로 csv 파일의 각 row를 나눌 때 자동적으로 알아서 따옴표 안에 있는 comma는 기준에서 제외
"""


import csv    # CSV module (built-in)

students = []


#1) csv.reader()
with open("students2.csv") as file:
    reader = csv.reader(file)    # list of lists
    for name, home in reader:    # reader에는 2개의 column이 있으므로 두 변수 설정
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):    # sort by name
    print(f"{student['name']} is in {student['home']}")


print()   # new line


#2) csv.DictReader()
with open("students2.csv") as file:
    reader = csv.DictReader(file)    # list of dicts
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})    # == students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
