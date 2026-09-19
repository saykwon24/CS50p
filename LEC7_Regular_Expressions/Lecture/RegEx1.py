"""
Regular Expression(RegEx): user input 등의 data가 유효한지 검증할 수 있도록 코드에서 정의한 'pattern'

re: regex를 위한 library    (https://docs.python.org/3/library/re.html)
    re.search(pattern, string, flags=0):    (일반적으로 사용자가 입력한) string에서 pattern을 검색하는 함수
    re.match(pattern, string, flags=0):     re.search()와 유사하지만, 기본적으로 string의 시작 부분부터 자동으로 pattern을 매칭하는 함수
                                            따라서 string의 시작 부분부터 일치시키려는 경우 regex의 맨 처음에 ^ 기호를 지정할 필요가 없음
    re.fullmatch(pattern, string, flags=0): string의 시작 부분뿐만 아니라 끝 부분도 일치시키는 함수로, ^과 $ 기호를 지정할 필요 없음
        <pattern으로 쓰이는 symbol, syntax>
        .         |  any character except a newline
        *         |  0 or more repetitions (on the left)
        +         |  1 or more repetitions (on the left) (== .*)
        ?         |  0 or 1 repetition (on the left)    >>> represent optional
        {m}       |  m repetitions
        {m, n}    |  m-n(m to n) repetitions
        ^         |  matches the start of the string
        $         |  matches the end of the string (or just before the newline at the end of the string)
        []        |  set of characters (no need seperator like comma), can express the range using '-'
        [^]       |  complementing the set (no need seperator like comma)
        \w        |  alphanumeric symbol or the underscore, 'any word character' (== [a-zA-Z0-9_])
        \W        |  not a word character
        \d        |  decimal digit (0~9)
        \D        |  not a decimal digit
        \s        |  whitespace characters (space, Tab, ...)
        \S        |  not a whitespace character
        A|B       |  either A or B
        (...)     |  a group, capturing version
        (?:...)   |  non-capturing version
        (?P<...>) |  give group a name to refer to later
        
        <flag로 쓰이는 built-in variable>
        re.IGNORECASE  |  treat case-insensitively
        re.MULTILINE   |  match a text that is multiple lines
        re.DOTALL      |  can configure the dot to recognize not just any character except newlines but any character plus newlines as well


Undeterministic : start state에서 시작해서 각 edge에서 character를 반복한 후, 최종적으로 double circle이 있는 accept state(final state)에 도달하는 일종의 state machine
Finite Automaton  double circle은 사용자의 입력을 다 읽은 후의 accept state에 있고, 해당 입력이 유효한 것임을 의미
                  single dot(.)은 character 1개를 소비한다는 것을 의미
                  (강의자료 그림 참고)


Escape Character '\': 컴퓨터에게 backslash 바로 뒤의 character를 특별한 의미로 취급하지 말고, 문자 그대로(literally) 취급하라고 알려주는 역할

r"": regular expression을 raw string(literally)으로 처리하도록 지정한다는 것을 의미
     backslash가 escape sequence가 시작된다는 것으로 판단하는 것을 막기 위함
     따라서 regex는 raw string으로 작성하고, 하나씩 차근차근 기능을 추가해 나가는 것을 권장
"""


import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
