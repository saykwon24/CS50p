"""
re.sub(pattern, repl, string, count=0, flags=0)
    stirng에서 pattern을 찾아 해당 부분을 repl로 대체하여 반환하는 함수

re.split(pattern, string, maxsplit=0, flags=0)
    특정 문자를 기준으로 string을 나누는 함수

re.findall(pattern, string, flags=0)
    string의 여러 위치에서 동일한 pattern의 여러 copy를 찾아 반환하는 함수
"""

import re

url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")