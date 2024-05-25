import tkinter as tk
from tkinter import simpledialog
window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def caesar_encode(text):
    result = []
    for char_ in text:
        char = ord(char_)
        if char > 96 and char <123:
            char -= 32
        if char < 65 or char > 90:
            return "알 수 없음"
        elif 88 <= char <= 90:
            char -= 23
        else:
            char += 3
        result.append(chr(char))
    return result


def main():
    text = gui_input("영어를 입력하세요(대/소문자 구별하지 않습니다.): ")
    result = "".join(caesar_encode(text))
    print(f"암호: {result}")


if __name__ == "__main__":
    main()