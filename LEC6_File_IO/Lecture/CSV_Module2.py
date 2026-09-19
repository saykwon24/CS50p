"""
csv.writer(csvfile): 사용자의 입력을 list 형태의 str로 바꾸어 csvfile에 저장하는 writer object를 반환
object.writerow(list): list의 element를 comma로 구분하여 하나의 string으로 연결하고, writer object에 하나의 row를 작성 (데이터를 한 줄씩 작성)
object.writerows(2dList): 2dList의 각 element에 대해 writerow를 실행 (데이터 전체를 한 번에 작성)
    >>> 각 row가 list로 표현되어 있는 데이터를 csv 파일에 쓸 수 있음

csv.DictWriter(f, fieldnames): 사용자의 입력을 dict 형태의 str로 바꾸어 f에 저장하는 object를 반환 (dictionary와 output row를 mapping)
                               fieldnames에 주어진 list를 dict의 key로 설정하고, key에 해당하는 value를 입력하여 csv 파일을 쓸 수 있음
object.writeheader(): object가 가리키는 csv 파일의 첫 번째 row에 항목의 이름(header)을 넣는 method
    >>> 각 row가 dict로 표현되어 있는 데이터를 csv 파일에 쓸 수 있음
"""


import csv


name = input("What's your name? ")
home = input("Where's your home? ")


#1) csv.writer()
with open("students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


#2) csv.DictWriter()
with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})