"""
raise: 의도적으로 직접 예외를 발생시켜 원하는 동작을 하도록 만드는 keyword
    >>> raise ErrorName("txt"): ErrorName과 함께 txt를 terminal에 출력
"""

def main():
    pace = get_pace(miles=26.2, minutes=180)    # 함수의 parameter에 직접 변수와 그 값을 지정 (default 설정)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid value for minutes.")
    
    return minutes / miles


main()