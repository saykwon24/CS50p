"""
Lambda Function: anonymous(익명의, 이름이 없는) function
                 code에서 한 곳에서만 일시적으로 call하면 function에 이름을 붙일 필요가 없으므로, 이 경우 사용
    >>> lambda argment: returnValue
"""


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student["name"]):    # CSV1.py의 get_name() 함수와 동일하게 작용
    print(f"{student['name']} is in {student['house']}")
