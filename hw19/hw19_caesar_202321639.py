import tkinter as tk
from tkinter import simpledialog, messagebox




def gui_input(text: str) -> str:
    return simpledialog.askstring(title="caesar 암호 변환기", prompt=text)



def caesar_encode(text):
    result = []
    for char_ in text:
        char = ord(char_)
        if (char >= 65 and char <= 87) or (char >= 97 and char <= 119):
            char += 3
        elif (char >= 88 and char <= 90) or (char >= 120 and char <= 122):
            char -= 23
        else:
            return "변환할 수 없는 문자가 입력되었습니다."
        result.append(chr(char))
    return result


def main():
    window = tk.Tk()
    window.withdraw()
    text = gui_input("영어를 입력하세요: ")
    result = "".join(caesar_encode(text))
    messagebox.showinfo(f"Result", f"암호: {result}")


if __name__ == "__main__":
    main()
