"""
Casting: data의 type을 일시적으로 바꾸는 함수
    str(x): x의 data type을 string으로 바꾸는 함수
    int(x): x의 data type을 integer로 바꾸는 함수
    float(x): x의 data type을 floating-point value로 바꾸는 함수
        >>> integer documentation: https://docs.python.org/3/library/functions.html?highlight=float#int
        >>> float documentation: https://docs.python.org/3/library/functions.html?highlight=float#float

round(number[, ndigits]): number를 가장 가까운 정수로 반올림하여 소수점 아래 ndigits까지 반환하는 함수
pow(x, n): x의 n제곱을 반환하는 함수
"""


x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)
print(z)

z = x / y
print(f"{z:,}")      # 숫자를 3자리씩 콤마로 구분
print(f"{z:.2f}")    # 소수점 이하 둘째자리까지 나타냄



# Function Definition
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n ** 2
    #return n * n
    #return pow(n, 2)


main()