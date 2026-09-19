"""
Tuple: list처럼 여러 데이터를 저장할 수 있는 data structure, 그러나 값을 추가/할당하거나 변경 불가능(immutable)
       변수의 값을 변경할 필요가 없거나, 효과적으로 여러 값을 반환할 때 comma를 사용하여 tuple 형태로 반환 (명시적으로 괄호를 사용하여 나타내기도 함)
       list와 마찬가지로 square braket으로 indexing 가능, 0부터 시작

많은 데이터를 지정하는 경우 tuple, list보다는 dict를 사용하여 key-value pair를 만들어 쉽게 접근할 수 있도록 하는 것이 좋음
"""


def main():
    student = get_student()
    
    #1) using tuple
    print(f"{student[0]} from {student[1]}")
    
    #2) using dict
    print(f"{student['name']} from {student['house']}")    # 따옴표 구분 주의


def get_student():
    name = input("Name: ")
    house = input("House: ")
    
    #1) using tuple
    return (name, house)    # return tuple
    
    #2) using dict
    return {"name": name, "house": house}    # return dict


if __name__ == "__main__":
    main()