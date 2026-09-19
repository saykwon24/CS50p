"""
input(str): str를 terminal에 출력한 후 사용자로부터 입력을 받아 string으로 반환하는 함수
print(str, sep=' ', end='\n'): comma를 기준으로 여러 argument가 있으면 sep로 나누고, str을 출력한 후 new line


<String Methods>
    .strip(): str의 좌,우에 있는 whitespace(space, new line 등) 제거
    .rstrip(): str의 오른쪽 whitespace 제거
    .lstrip(): str의 왼쪽 whitespace 제거
    .title(): 공백을 기준으로 string의 첫 글자를 capitalize
    .split(str): str를 기준으로 string을 분리하여 list로 반환, default=" "
        >>> string documentation: https://docs.python.org/3/library/stdtypes.html#str


Format String: 'f'와 'curly braces({})'를 사용하여 string에 변수 등을 삽입할 수 있는 기능
"""


name = input("What's your name? ").strip().title()

first, last = name.split(" ")

#print("hello, David")
#print("hello, " + name)    # '+' operator 사용 시 공백 없이 연결
#print("hello,", name)      # comma로 여러 argument 입력 시 공백으로 분리하여 연결
print(f"hello, {first}")