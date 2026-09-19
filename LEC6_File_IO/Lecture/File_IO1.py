"""
File I/O: 파일을 input으로 받거나, 새로운 파일을 output으로 생성하는 프로그램의 ability
          파일의 형태로 저장하므로 프로그램이 종료되어도 PC나 클라우드 서버 등에 저장되어 사라지지 않음


open(filename, mode, encoding="utf-8", newline="")
    filename을 mode의 모드로 열어 file handle을 반환 (file handle: 나중에 해당 파일에 액세스할 수 있도록 하는 특수한 값)
    filename에 해당하는 파일이 없으면 새로 생성
    mode: "r" == 읽기[default], "w" == 덮어쓰기, "a" == 내용 추가
    encoding: utf-8로 저장된 데이터를 cp949로 읽으려고 하면 error가 발생하므로, 이 경우 명시적으로 인코딩 제시
    newline: windows에서는 바이너리 모드가 아닌 경우 csv.writer()가 \n을 \r\n으로 치환하여 \r\r\n이 되므로, "w" 모드에서는 argument에 'newline=""'을 추가하여 해결
    파일을 open한 후에는 반드시 close를 해줘야 함


<File I/O 관련 method>
.close():          파일을 닫고 저장하는 method
.read():           파일 내부의 텍스트를 읽어 하나의 string으로 반환하는 method
.readlines():      파일 내부의 텍스트를 읽어 line 별로 나누어 element로 갖는 list로 반환하는 method
.write(str):       파일에 str를 쓰는 작업을 하는 method, 단일 string을 쓸 때 적합
.writelines(list): 파일에 line 별로 list의 element를 쓰는 작업을 하는 method
"""


name = input("What's your name? ")


file = open("names.txt", "a")
file.write(f"{name}\n")    # new line per input
file.close()
