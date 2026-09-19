"""
Inheritance: 한 class가 variable, method 등의 attribute들을 공통적인 특징이 있는 다른 class의 것을 가져와 사용하는 개념
             여러 class 간의 계층 구조를 만들어 중복되는 부분을 줄일 수 있음
             상속받는 class를 subclass, 상속하는 class를 superclass라고 지칭
             class 정의 시 "subclass(superclass)"와 같이 작성하여 subclass가 superclass로부터 상속받음을 알림
             "super().superMethod(arg, ...)"와 같이 작성하여 superclass의 method를 참조할 수 있음

exception도 계층 구조로 이루어져 있어, 여러 error를 처리하고 싶을 때 parent exception을 처리하면 쉽게 여러 error 처리 가능
    BaseException
     +-- KeyboardInterrupt
     +-- Exception
          +-- ArithmeticError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- KeyError
          +-- NameError
          +-- SyntaxError
          |    +-- IndentationError
          +-- ValueError
    ...
"""


# Superclass (parent)
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    
    ...


# Subclass 1
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)   # reference to __init__ method of the superclass 'Wizard'
                                 # and then passed 'name' of this class 'Student'
        self.house = house
    
    ...


# Subclass 2
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)    # same as Student
        self.subject = subject
        
    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")