"""
List: 하나의 변수에 여러 값을 저장할 수 있는 data structure, squart braket([])으로 표현
      list(), [] 등으로 initialize
      list name 뒤에 square braket으로 list indexing, 1번째 element의 index는 0부터 시작 (LIST[0])
    >>> list documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

len(s): s의 크기(원소의 개수)를 반환하는 함수
"""


students = ["Hermione", "Harry", "Ron"]

# Print only element of list
for student in students:
    print(student)

# Print index and element of list
for i in range(len(students)):
    print(i + 1, students[i])    # list indexing
