class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # get_student() in OOP2.py -> capsulizing in class
    @classmethod
    def get(cls):    # can call this method without instantiating an object first
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)    # instantiate class's object by using 'cls' that is passed in (conventionally)
                                   # can also use 'Student(class's name)' instead of 'cls'
                                   # initialize the object with the arguments(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()