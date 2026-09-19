distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    
    try:
        au = float(distances[spacecraft])
    except KeyError:      # 입력한 것이 dict의 key에 없는 경우
        print(f"'{spacecraft} is not in dictionary")
    except ValueError:    # Pioneer 10, 11을 입력할 경우
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    
    m = convert(au)
    print(f"{m} m away")


def convert(au):
    return au * 149597870700
        # au가 str이면 메모리 주소에 곱하기 연산을 하게 되어 MemoryError


main()