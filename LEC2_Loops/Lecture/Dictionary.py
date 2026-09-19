""""
Dictionary: 사전에 단어-정의 쌍이 있듯이, key-value의 형태로 저장되는 data structure, curly braces({})로 표현
            dict(), {} 등으로 initialize
            dict name 뒤에 square braket에 key를 indexing하여 대응햐는 value를 나타냄 (DICT["key"] == value)
            list가 1차원 행렬이라면 dict는 2차원 행렬
    >>> dictionary documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
"""


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:    # student는 students dict의 key를 가져옴
    print(student, students[student], sep=",")
