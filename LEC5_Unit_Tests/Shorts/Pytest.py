def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    
    print(f"{au} AU is {convert(au)} m")
    

def convert(au):
    # isinstance(var, (CASE1, CASE2, ...)): var이 CASE에 속하면 True, 그렇지 않으면 False 반환
    if not isinstance(au, (int, float)):
        raise TypeError("au must ve an int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()