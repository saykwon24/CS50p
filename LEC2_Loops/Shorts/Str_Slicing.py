"""
String Slicing: square braket에서 colon과 index를 이용해서 string의 일부만을 가져오는 방법
                string의 첫 글자의 index == 0, 맨 마지막 글자의 index == -1
                처음과 끝을 지정하지 않으면 각각 처음부터/끝까지 slicing
"""


def main():
    phone = "+1 617-495-1000"
    
    print(phone[-4:])    # string slicing


main()