def main():
    with open("alice.txt", "r") as f:
        #contents = f.read()
        contents = f.readlines()
    
    
    chapter1 = contents[52:270]    # index는 0부터 시작하므로 주의
    
    with open("chapter1.txt", "w") as f:
        #f.write("Chapter 1.")
        f.writelines(chapter1)


main()