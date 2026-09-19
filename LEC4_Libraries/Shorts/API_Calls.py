import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}    # query parameter로 artist를 전달
        )
        response.raise_for_status()    # raise_for_status(): 요청이 성공했는지 확인, 실패하면 예외 발생 (HTTPError)

    except requests.HTTPError:         # HTTPError: 요청이 실패했을 때 발생 (인터넷 연결 문제 등)
        print("Couldn't complete request!")
        return
    
    #print(response)                   # 200: 요청이 성공적으로 처리되었다는 것을 알려주는 HTTP 상태 코드
    content = response.json()          # JSON 형식의 response 본문을 파이썬 객체로 변환
    for artwork in content["data"]:    # "data" 키에 해당하는 값은 artwork의 리스트
        print(f"* {artwork['title']}")


main()