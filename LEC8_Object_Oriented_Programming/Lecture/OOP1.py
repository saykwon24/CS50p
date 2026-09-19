"""
Object-Oriented Programming(OOP): 데이터와 그 데이터를 조작하는 함수(method)를 하나의 object로 묶어 관리하는 프로그래밍 패러다임
                                  이전까지는 어떤 기능을 어떤 순서로 처리할 것인지를 중심으로 한 '절차 지향'이었다면, 
                                  '객체 지향'은 기능이 아닌 객체가 중심이 되어 어떤 객체가 어떤 역할을 할 것인지에 중점


Class: 사용자가 원하는 대로 data type을 정의하여 이름을 붙일 수 있는 '틀', 관례적으로 class name의 첫 글자는 대문자로 작성
       (함수처럼) class에 parameter를 전달하여 해당 object의 내용을 customize(사용자 정의)할 수 있음
       class의 attribute를 추가할 때 모든 data type이 가능 (str, int, float, ...)
       attribute에 접근하려면 'dot notation'을 이용 (object.attr)
       class에는 attribute, instance뿐만 아니라 method(class 내부에 정의된 함수)도 포함
    >>> https://docs.python.org/3/tutorial/classes.html

Object(instance): class라는 '틀'을 구체화/실체화한 것, 하나의 class에 여러 개를 정의할 수 있음
                  동일한 class의 object는 동일한 구조를 가짐
                  object는 변경 가능(mutable)하지만 변경 불가능(immutable)하게 만들 수 있음

        >>> class Class:
        ...     def __init__(self, arg1, arg2, ...):
        ...         self.arg1 = arg1
        ...         self.arg2 = arg2
        ...
        ... object = Class(arg1, arg2, ...)
            * Class를 호출하여 arg1, arg2, ...를 전달 
                -> Python은 자동으로 constructor(생성자)인 __init__ method를 호출하여 object를 구성 (instantiate an object) 
                -> 컴퓨터의 메모리에 object 저장
            * Class 내에 attribute(instance variable)을 생성 
                -> 전달받은 argument를 활용하여 attribute에 값을 추가/할당 
                -> Class 내의 모든 attribute를 동일한 이름의 object에 저장


Instance Methods
    object.__init__(self, ...): class의 object 내용을 initialize(instantiate)할 때 사용하는 method, Python이 자동으로 호출
                                self는 self 뒤에 오는 argument들을 object의 attribute의 값으로 할당하여 저장하고 접근할 수 있도록 하는 argument
                                즉, 현재 object에 대한 참조(reference)를 전달하여 해당 object 내부로 들어갈 수 있음
                                dict와는 달리, object initialization 시에 invalid한 값이 들어왔을 때 의도적으로 error를 발생시키면(예외 처리) 정확히 제어할 수 있다는 장점
    object.__str__(self): 다른 function이 object를 str 형식으로 읽어들일 수 있도록 하는 method

사용자가 class 내에 method를 직접 정의하여 사용 가능
    적어도 하나의 argument가 필요한데, 관례적으로는 self를 사용함
"""


class Student:
    def __init__(self, name, house, patronus):    # constructor
        # Treat invalid name and house
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Make own instance method(function)
    def charm(self):    # need at least one argument 'self' (conventionally)
        match self.patronus:
            case "Stag":
                return "**S**"
            case "Otter":
                return "**O**"
            case "Jack Russell terrier":
                return "**J**"
            case _:
                return "sizzle"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    """
    # call the class and instantiate(create) an object of the class
    student = Student()
    
    # store(add) attributes in the class
    student.name = input("Name: ")      # name attribute
    student.house = input("House: ")    # house attribute
    """
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()