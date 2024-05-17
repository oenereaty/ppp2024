def caesar_encode(text):
    result = []
    for char_ in text:
        char = ord(char_)
        if char > 96 and char <123:
            char -= 32
        if char < 65 or char > 90:
            return "암호로 변환할 수 없습니다"
        elif 88 <= char <= 90:
            char -= 23
        else:
            char += 3
        result.append(chr(char))
    return result


def main():
    text = input("영어를 입력하세요(대/소문자 구별하지 않습니다.): ")
    print(f"암호는{caesar_encode(text)}!")


if __name__ == "__main__":
    main()