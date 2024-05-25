import random
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def lotto():
    result = []
    while len(result) < 6:
        i = random.randint(1, 45)
        if i not in result:
            result.append(i)
    return sorted(result)


def main():
    n = int(gui_input("몇 회 추출하시겠습니까?:"))
    for i in range(n):
        print(f"{i + 1}번 로또 번호:{lotto()}")


if __name__ == "__main__":
    main()
