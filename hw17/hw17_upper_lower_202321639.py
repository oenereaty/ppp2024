import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def toggle_text(text):
    result = []
    for char_ in text:
        char = ord(char_)
        if char >= 65 and char <= 90:
            char += 32

        elif char >= 97 and char <= 122:
            char -= 32
        result.append(chr(char))
    return result


def main():
    text = gui_input("영어를 입력하세요: ")
    result = "".join(toggle_text(text))
    print(f"대소문자 변환 결과: {result}")


if __name__ == "__main__":
    main()
