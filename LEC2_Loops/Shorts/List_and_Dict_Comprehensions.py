from helpers import get_words, save_counts

def main():
    words = get_words("address.txt")
    
    # List Comprehension
    lowercase_words = [word.lower() for word in words if len(word) > 4]
        # if 조건이 참일 때 words의 word를 lowercase로 변환하여 list에 저장
    
    # Dictionary Comprehension
    counts = {word: lowercase_words.count(word) for word in lowercase_words}
        # word == key, lowercase_words.count(word) == value로 dict에 저장
    
    save_counts(counts)


main()    # terminal 창에 '.\counts.csv' 입력 -> 연결 프로그램 VS Code로 실행