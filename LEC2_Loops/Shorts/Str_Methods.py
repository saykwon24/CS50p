"""
'str'.join(list): list element를 결합하는 데 사용할 str을 지정하는 method
    >>> 이외의 methods는 LEC0/Lecture/string.py 참고
"""


SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))


main()