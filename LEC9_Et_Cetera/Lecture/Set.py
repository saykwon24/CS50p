"""
Set: 중복되는 값이 없는 데이터들의 집합, data type
     set에 저장되는 데이터들은 무작위로 배열됨 ('dis'enumerate)
    >>> https://docs.python.org/3/library/stdtypes.html#set

<set methods>
set.add(element): set에 element를 추가하는 method
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)