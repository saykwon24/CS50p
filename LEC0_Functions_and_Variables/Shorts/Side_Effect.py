"""
Side Effect: 값을 return하는 것이 아닌 함수가 실행되는 동안 변경되는 모든 것

global: 해당 함수 내에서 접근하고 수정할 수 있는 전역 변수를 지정하는 keyword
        값을 return하는 것이 아닌 함수가 실행되는 동안 side effect로서 작용
"""


emoticon = "v.v"    # global variable


def main():
    global emoticon    # global keyword
    
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()