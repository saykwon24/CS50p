# Lists of Dictionaries: 3차원 행렬
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}    # None(""): 값이 없다는 것을 나타내는 keyword
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
    # list의 각 원소가 dict이므로, element of list인 student에 indexing을 해야 함
