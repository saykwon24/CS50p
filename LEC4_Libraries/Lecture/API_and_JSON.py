"""
APIs: 코드를 작성하여 통신할 수 있는 third party services
      인터넷 등에서 API를 통해 다른 곳의 서버에서 일부 데이터를 가져와(parsing) 나의 프로그램에서 사용
      requests Library를 설치하여 사용: 'pip install requests'

requests Library
    requests.get(URL): URL의 서버로부터 응답을 받는 함수, HTTP GET 요청을 보냄
>>> documentation: https://docs.python-requests.org/


JSON: JavaScript Object Notation, 표준 텍스트 기반 데이터 포맷
      컴퓨터 간에 데이터를 교환할 때 language에 구애받지 않고 사용됨
      json Library가 python에 내장되어 있음
>>> JSON documentation: https://docs.python.org/3/library/json.html

json Library
    response.json(): response를 JSON 형식으로 변환하는 함수 (JSON 객체 반환)
    json.dumps(): JSON 객체를 string으로 변환하는 함수
"""


import json
import requests
import sys

# Error handling
if len(sys.argv) != 2:
    sys.exit()

# Get response from server(URL)
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

print(json.dumps(response.json(), indent=2))    # indent=2: JSON을 보기 좋게 2칸 들여쓰기

o = response.json()    # JSON object
for result in o["results"]:
    print(result["trackName"])
