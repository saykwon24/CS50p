"""
Decorator: 함수를 'decorate', 즉 다른 함수의 동작을 modify하는 함수 (@ syntax 등)

Property: 좀 더 defensive한 mechanism으로 구성된 attribute, getter와 setter를 class 내에 정의하여 property로 define
          class를 호출하고 한참 뒤에 object의 instance variable을 invalid한 값으로 바꾸는 것을 방지할 수 있어, 일반적인 attribute보다 more defensive
          [before] attribute -> getter and setter are defined -> [after] property

Getter: a function for a class that gets some attributes
        "@property"를 함수 위에 추가하여 getter로 쓸 것임을 알림
        property의 이름과 정확히 같은 이름으로 함수의 이름을 설정 -> 자동적으로 새로운 decorator 생성

Setter: a function in some class that sets some value
        "@decoName.setter"를 함수 위에 추가하여 setter로 쓸 것임을 알림 (decoName는 getter가 생성한 decorator, 즉 getter의 이름과 동일)
        getter의 이름과 같게 설정하여, 해당 property에 access하기 전에 setter을 자동으로 호출하여 error 처리
        argument로는 self 외에 error 처리를 할 값을 넣음


다른 언어와는 달리, Python은 'honor system'
    코드의 공개 범위(공개, 비공개)에 대한 개념, visibility에 대한 개념이 존재하지 않음
    따라서 관례적으로만 instance variable의 앞에 '_'이 1개 이상 있으면 건들지 말라는 의미, 비공개의 의미로 사용됨
"""


class Student:
    def __init__(self, name, house):
        self.name = name      # property
        self.house = house    # property
                              # automatically call the setter in __init__
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):    # Getter for name
        return self._name
    
    @name.setter
    def name(self, name):    # Setter for name
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property
    def house(self):    # Getter for house
        return self._house
    
    @house.setter
    def house(self, house):    # Setter for house
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house    # have the setter not overwrite the value 'house' to instance variable 'self.house'
                               # so instance variable's name must be different with property's name, 'house'
                               # conventionally put '_' in front of instance variable's name


def main():
    student = get_student()
    """
    student.house = "Number Four, Privet Drive"    # assign or 'set' a value
                                                   # 'house' is defined as a property
                                                   # then automatically call the setter, and have to go through it
    """
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()