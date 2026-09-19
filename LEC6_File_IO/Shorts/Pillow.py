from PIL import Image
from PIL import ImageFilter    # 다양한 이미지 필터를 적용할 때 사용하는 class


def main():
    with Image.open("in.jpeg") as img:    # image object
        print(img.size)      # pixel 단위로 img의 size 출력
        print(img.format)    # img의 파일 형식을 출력
        
        img = img.rotate(180)                       # img를 180도 회전
        img = img.filter(ImageFilter.BLUR)          # 이미지를 블러 처리 (흐릿하게)
        img = img.filter(ImageFilter.FIND_EDGES)    # 이미지의 가장자리를 하이라이트 (강조)
        img.save("out.jpeg")                        # img를 'out.jpeg'이라는 파일명으로 저장


main()