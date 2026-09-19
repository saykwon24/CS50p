from package.module import get_artworks, get_artists    # 'package' package의 'module' 모듈에서 함수를 가져옴


def main_1():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")


def main_2():
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"* {artist}")


main_1()
main_2()