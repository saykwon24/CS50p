"""
Binary File: 0과 1로 구성된 파일로, 0과 1을 원하는 패턴으로 배치할 수 있음
             텍스트가 아닌 이미지, 오디오 또는 비디오 정보를 저장하려는 경우 유용

Pillow(PIL) Library: 이미지 파일을 저장하는 데 유용한 module
    .save(filename, save_all=True, append_images, duration, loop): 이미지 파일 열기, 닫기, 저장을 모두 처리하는 함수
                                                                   filname으로 이미지 저장
                                                                   save_all: True이면 사진 모두 저장
                                                                   append_images: 추가할 이미지, list 형태로 지정
                                                                   duration: 사진 당 지속되는 시간 [ms]
                                                                   loop: 반복할 횟수, 0이면 무한 반복
"""


import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)    # open image file
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)