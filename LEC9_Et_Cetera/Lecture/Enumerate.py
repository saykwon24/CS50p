"""
enumerate(iterable, start=0): iterable의 인덱스와 값을 반환하는 함수, 인덱스는 start부터 시작
    >>> https://docs.python.org/3/library/functions.html#enumerate
"""


students = ["Hermione", "Harry", "Ron"]

# Dictionary Comprehension
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]    # list of dicts
gryffindors = {student: "Gryffindor" for student in students}    # dicts
print(gryffindors)


# enumerate
for i, student in enumerate(students):
    print(i + 1, student)
