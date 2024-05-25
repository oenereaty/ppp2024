import time
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()



def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def gui_input(text):
    return simpledialog.askstring(title="Test", prompt=text)


def main():
    count = int(gui_input("카운트 할 시간 설정:"))

    while True:
        print(f"카운트 다운...{count}초!")
        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    print("Bomb!")


if __name__ == "__main__":
    main()
