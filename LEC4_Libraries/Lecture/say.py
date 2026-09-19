def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


# __name__: command line에서 파일을 실행할 때, python에서 자동으로 값이 "__main__"으로 설정되는 특수 변수
# 따라서 다른 파일에서 이 파일(6_say.py)을 실행하는 경우에는 if문이 실행되지 않음
if __name__ == "__main__":
    main()