"""
filter(function, iterable): map() 함수와 마찬가지로 function을 element of sequence에 적용
                            map() 함수와 달리 filter() 함수의 function argument에는 True/False를 반환하는 함수를 넣어 각 element의 포함 여부를 결정
    >>> https://docs.python/org/3/library/functions.html#filter
"""


students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]


# Using list comprehension
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)



# Using filter() function (more functional approach)
def is_gryffindor(s):
    return s["house"] == "Gryffindor"
gryffindors = filter(is_gryffindor, students)    # pass function is_gryffindor by its name as arg, not call

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)    # same as line 28 to 30

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
