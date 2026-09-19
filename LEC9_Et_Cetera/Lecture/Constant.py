"""
python은 'honor system'이므로 다른 언어와 달리 값을 바꿀 수 없는 변수인 constant를 강제하지 않음
대신에 변수의 이름을 uppercase로 설정하여 해당 변수가 상수임을 나타냄
"""


class Cat:
    MEOWS = 3    # class constant
    
    def meow(self):
        for _ in range(Cat.MEOWS):    # how to use class variable in instance method
            print("meow")


cat = Cat()
cat.meow()