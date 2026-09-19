"""
List Methods
    .append(element):    list에 element를 추가하는 method
    .remove(element):    list의 element를 제거하는 method
    .extend(LIST):       기존 list에 LIST를 이어붙여 확장하는 method, 여러 element를 추가할 때 사용
    .insert(n, element): list의 n번째 index에 element를 삽입하는 method
    .reverse():          list의 element 순서를 반대로 뒤집는 method
"""

results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])

results.extend(["Bowser", "Donkey Kong Jr."])

results.remove("Bowser")
results.insert(0, "Bowser")

results.reverse()

print(results)