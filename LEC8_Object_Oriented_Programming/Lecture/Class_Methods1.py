"""
class는 주로 현실이나 가상 세계의 어떤 실체(entity)를 표현하고자 할 때 사용

Class Method: 특정 객체의 값이나 인스턴스 변수와 관계없이, 클래스 자체와 연관된 기능을 수행하는 method
              객체, self에 접근할 수 있는 인스턴스 변수가 아닌 class method이지만, 어떤 class에 속하는 지는 알고 있음
              class의 object를 지정하지 않고(class가 무엇인지만 알고 object가 하나도 없음), 특정 기능이나 데이터만을 가지는 class를 만들 때 사용
              "@classmethod"를 method 위에 추가하여 class method임을 알리고, self argument 대신 'cls' argument 대입하여 class 자체에 대한 참조(reference)를 알림
              특정 객체를 초기화하는 method인 __init__이 필요하지 않음

instance variable <-> class variable / instance method <-> class method
instance variable, method는 특정 object에 속해 있거나 작동하는 반면, class variable, method는 class 전체에서 작동하므로, 해당 class의 모든 object에서 동작


이외에도 static method(@staticmethod) 등의 다양한 method가 존재
"""


import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]    # class variable
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")    # Just use the class's functionality