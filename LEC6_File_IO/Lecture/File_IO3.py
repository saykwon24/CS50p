"""
sorted(list, reverse=False): list를 alphabetically sort하는 function
                             reverse: False == 오름차순[default], True == 내림차순
"""


#1) 파일을 line 별로 하나의 list에 모은 후 정렬하는 방법
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names):
    print(f"hello, {name}")


#2) 파일 자체에서 정렬하는 방법
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"hello, {line.rstrip()}")
