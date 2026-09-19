def area(length, width):
    print(str(length * width) + " square feet")
    return length * width    # return은 해당 함수가 끝났다는 것도 의미함


def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " square feet")


main()