"""
with ... as ...: 파일을 close하는 것을 잊어버리는 것을 방지하기 위한 keyword, indent 되어있는 동안만 파일을 open
                 file handle을 저장하는 변수는 as 뒤에 배치
"""


with open("names.txt", "r") as file:
    lines = file.readlines()    # save as list

for line in lines:
    print("hello,", line.rstrip())
        # file에 텍스트를 추가할 때 new line을 함께 넣었으므로, 총 2번 줄바꿈해서 출력됨
        # lines의 element는 string이므로 '.rstrip()' method를 이용하여 new line 제거


"""
# 하나로 합친 버전
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""